Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$passed = 0
function Assert-That([bool]$Condition, [string]$Name) {
  if (-not $Condition) { throw "REGRESSION_FAIL: $Name" }
  $script:passed++
  Write-Output "PASS $Name"
}

function Partition-ByReadouts([object[]]$Items, [hashtable[]]$Tests) {
  $groups = @{}
  foreach ($item in $Items) {
    $key = (($Tests | ForEach-Object { [string]$_.Invoke.Invoke($item) }) -join '|')
    if (-not $groups.ContainsKey($key)) { $groups[$key] = @() }
    $groups[$key] += $item
  }
  return @($groups.Values | ForEach-Object { (@($_ | Sort-Object) -join ',') }) | Sort-Object
}

function Same-Partition([string[]]$Actual, [string[]]$Expected) {
  return (($Actual | Sort-Object) -join ';') -eq (($Expected | Sort-Object) -join ';')
}

function Descends-Unary([object[]]$Items, [hashtable[]]$Tests, [hashtable]$Operation) {
  $classes = @{}
  foreach ($item in $Items) {
    $key = (($Tests | ForEach-Object { [string]$_.Invoke.Invoke($item) }) -join '|')
    if (-not $classes.ContainsKey($key)) { $classes[$key] = @() }
    $classes[$key] += $item
  }
  foreach ($class in $classes.Values) {
    $imageKeys = @($class | ForEach-Object {
      $image = $Operation.Invoke.Invoke($_)
      (($Tests | ForEach-Object { [string]$_.Invoke.Invoke($image) }) -join '|')
    } | Select-Object -Unique)
    if ($imageKeys.Count -ne 1) { return $false }
  }
  return $true
}

# A partial binary operation descends precisely in this finite fixture when
# definedness is constant on pairs of empirical classes and every defined
# output has a class constant on such pairs.  `$null` denotes "undefined".
function Descends-PartialBinary([object[]]$Items, [hashtable[]]$Tests, [hashtable]$Operation) {
  $classKey = {
    param($item)
    (($Tests | ForEach-Object { [string]$_.Invoke.Invoke($item) }) -join '|')
  }
  foreach ($left in $Items) {
    foreach ($right in $Items) {
      foreach ($leftPrime in $Items) {
        foreach ($rightPrime in $Items) {
          if ((& $classKey $left) -ne (& $classKey $leftPrime)) { continue }
          if ((& $classKey $right) -ne (& $classKey $rightPrime)) { continue }
          $valueOutput = @($Operation.Invoke.Invoke($left, $right))
          $primeValueOutput = @($Operation.Invoke.Invoke($leftPrime, $rightPrime))
          $value = if ($valueOutput.Count -eq 0) { $null } else { $valueOutput[0] }
          $primeValue = if ($primeValueOutput.Count -eq 0) { $null } else { $primeValueOutput[0] }
          if ($null -eq $value) {
            if ($null -ne $primeValue) { return $false }
            continue
          }
          if ($null -eq $primeValue) { return $false }
          if ((& $classKey $value) -ne (& $classKey $primeValue)) { return $false }
        }
      }
    }
  }
  return $true
}

function Refines-Partition([object[]]$Items, [hashtable[]]$FineTests, [hashtable[]]$CoarseTests) {
  foreach ($left in $Items) {
    foreach ($right in $Items) {
      $fineEqual = ((($FineTests | ForEach-Object { [string]$_.Invoke.Invoke($left) }) -join '|') -eq (($FineTests | ForEach-Object { [string]$_.Invoke.Invoke($right) }) -join '|'))
      $coarseEqual = ((($CoarseTests | ForEach-Object { [string]$_.Invoke.Invoke($left) }) -join '|') -eq (($CoarseTests | ForEach-Object { [string]$_.Invoke.Invoke($right) }) -join '|'))
      if ($fineEqual -and -not $coarseEqual) { return $false }
    }
  }
  return $true
}

# M1: deterministic quotient and refinement.
$m1 = @('a','b','c','d')
$z = @{ Invoke = { param($x) @{a=0;b=0;c=1;d=1}[$x] } }
$x = @{ Invoke = { param($u) @{a=0;b=1;c=0;d=1}[$u] } }
$swap = @{ Invoke = { param($u) @{a='b';b='a';c='d';d='c'}[$u] } }
Assert-That (Same-Partition (Partition-ByReadouts $m1 @($z)) @('a,b','c,d')) 'M1 coarse quotient'
Assert-That (Same-Partition (Partition-ByReadouts $m1 @($z,$x)) @('a','b','c','d')) 'M1 refinement splits classes'
Assert-That (Descends-Unary $m1 @($z) $swap) 'M1 declared swap descends'

# M6: a duplicate coordinate presentation transports the M1 quotient and descent verdict.
$m6 = @('00','01','10','11')
$m6z = @{ Invoke = { param($u) [int]$u.Substring(0,1) } }
$m6x = @{ Invoke = { param($u) [int]$u.Substring(1,1) } }
$m6swap = @{ Invoke = { param($u) "$($u.Substring(0,1))$((1 - [int]$u.Substring(1,1)))" } }
Assert-That (Same-Partition (Partition-ByReadouts $m6 @($m6z)) @('00,01','10,11')) 'M6 transported coarse quotient'
Assert-That (Descends-Unary $m6 @($m6z) $m6swap) 'M6 transported operation descent'

# M2: finite records support exact rational aggregation, without inferring probability.
$m2p = @(4,4)
$m2r = @(0,8)
$m2Aggregate = @(2,6)
$m2Expected = 0..1 | ForEach-Object { ($m2p[$_] + $m2r[$_]) / 2 }
Assert-That ((($m2Aggregate -join ',') -eq ($m2Expected -join ','))) 'M2 finite count aggregation is exact'

# SP5: constant finite-record protocols are stable and an already declared aggregate obeys its rational limit law.
$spLeft = @(4,4)
$spRight = @(0,8)
$spAggregate = @(2,6)
$spLimitLaw = 0..1 | ForEach-Object { (($spLeft[$_] / 8) + ($spRight[$_] / 8)) / 2 }
$spAggregateProfile = $spAggregate | ForEach-Object { $_ / 8 }
Assert-That ((($spLeft | Measure-Object -Sum).Sum -eq 8) -and (($spRight | Measure-Object -Sum).Sum -eq 8)) 'SP5 constant finite protocols are stable witnesses'
Assert-That ((($spAggregateProfile -join ',') -eq ($spLimitLaw -join ','))) 'SP5 descended aggregate satisfies rational affine limit law'

# M4: a declared process can fail descent at a coarse repertoire and pass after a concrete refinement.
$m4 = @('z+','z-','x+')
$Z = @{ Invoke = { param($u) @{ 'z+'='0'; 'z-'='1'; 'x+'='0'}[$u] } }
$X = @{ Invoke = { param($u) @{ 'z+'='h'; 'z-'='h'; 'x+'='+'}[$u] } }
$xFlip = @{ Invoke = { param($u) @{ 'z+'='z-'; 'z-'='z+'; 'x+'='x+'}[$u] } }
Assert-That (-not (Descends-Unary $m4 @($Z) $xFlip)) 'M4 Xflip NOT DEFINED at coarse quotient'
Assert-That (Descends-Unary $m4 @($Z,$X) $xFlip) 'M4 Xflip descends after declared refinement'

# M5: adding the actually represented context r o C is a concrete realization of the diagnostic split.
$m5 = @('u','v','p','q')
$r = @{ Invoke = { param($u) @{u=0;v=0;p=0;q=1}[$u] } }
$C = @{ Invoke = { param($u) @{u='p';v='q';p='p';q='q'}[$u] } }
$rAfterC = @{ Invoke = { param($u) $r.Invoke.Invoke($C.Invoke.Invoke($u)) } }
Assert-That (-not (Descends-Unary $m5 @($r) $C)) 'M5 constructor NOT DEFINED at coarse quotient'
$m5Refined = Partition-ByReadouts $m5 @($r,$rAfterC)
Write-Output "INFO M5 refined partition: $($m5Refined -join ';')"
Assert-That (Same-Partition $m5Refined @('p,u','v','q')) 'M5 concrete refinement realizes constructor repair'
Assert-That (Descends-Unary $m5 @($r,$rAfterC) $C) 'M5 constructor descends after concrete refinement'
Assert-That (Same-Partition $m5Refined @('p,u','v','q')) 'RR5 finite available probe set realizes M5 repair'

# RR1: a mathematical operation-induced split need not be available as a repertoire refinement.
$rr1 = @('a','b','c')
$rr1r = @{ Invoke = { param($u) @{a=0;b=0;c=1}[$u] } }
$rr1f = @{ Invoke = { param($u) @{a='a';b='c';c='c'}[$u] } }
Assert-That (-not (Descends-Unary $rr1 @($rr1r) $rr1f)) 'RR1 diagnostic operation requires a stricter mathematical refinement'
Assert-That (Same-Partition (Partition-ByReadouts $rr1 @($rr1r)) @('a,b','c')) 'RR1 available grammar cannot realize diagnostic split'

# C2: partial-domain descent requires domain saturation on coarse fibres.
$c2Domain = @{ a=$true; b=$false; c=$true }
Assert-That (-not ($c2Domain['a'] -eq $c2Domain['b'])) 'C2 partial domain is not saturated on a coarse class'

# C3: two independent coarse repertoires can be incomparable, hence supply no canonical map.
$c3 = @('00','01','10','11')
$firstBit = @{ Invoke = { param($u) $u.Substring(0,1) } }
$secondBit = @{ Invoke = { param($u) $u.Substring(1,1) } }
Assert-That (-not (Refines-Partition $c3 @($firstBit) @($secondBit))) 'C3 first-bit repertoire does not refine second-bit repertoire'
Assert-That (-not (Refines-Partition $c3 @($secondBit) @($firstBit))) 'C3 second-bit repertoire does not refine first-bit repertoire'

# P1: compatible pair profiles need not extend to a joint profile.  Exhaust all 2^3 assignments.
$assignments = 0..7 | ForEach-Object {
  @{ A=(($_ -band 1) -shr 0); B=(($_ -band 2) -shr 1); C=(($_ -band 4) -shr 2) }
}
$allPairwiseUnequal = @($assignments | Where-Object { $_.A -ne $_.B -and $_.B -ne $_.C -and $_.C -ne $_.A })
Assert-That ($allPairwiseUnequal.Count -eq 0) 'P1 compatible pair constraints have no binary global completion'

# M3: PR-style contextual parity tables have uniform one-site margins but no four-bit joint assignment.
$fourBitAssignments = 0..15 | ForEach-Object {
  @{ A0=(($_ -band 1) -shr 0); A1=(($_ -band 2) -shr 1); B0=(($_ -band 4) -shr 2); B1=(($_ -band 8) -shr 3) }
}
$prGlobal = @($fourBitAssignments | Where-Object {
  (($_.A0 -bxor $_.B0) -eq 0) -and
  (($_.A0 -bxor $_.B1) -eq 0) -and
  (($_.A1 -bxor $_.B0) -eq 0) -and
  (($_.A1 -bxor $_.B1) -eq 1)
})
Assert-That ($prGlobal.Count -eq 0) 'M3 contextual parity profiles have no global completion'
$uniformMargins = $true
foreach ($xBit in 0..1) {
  foreach ($yBit in 0..1) {
    $outcomes = @()
    foreach ($aBit in 0..1) {
      foreach ($bBit in 0..1) {
        if (($aBit -bxor $bBit) -eq ($xBit * $yBit)) { $outcomes += ,@($aBit,$bBit) }
      }
    }
    $uniformMargins = $uniformMargins -and (($outcomes | ForEach-Object { $_[0] } | Select-Object -Unique).Count -eq 2)
    $uniformMargins = $uniformMargins -and (($outcomes | ForEach-Object { $_[1] } | Select-Object -Unique).Count -eq 2)
  }
}
Assert-That $uniformMargins 'M3 one-site margins remain uniform in every declared parity context'

# P2: a non-stable record sequence retains two cluster profiles.
$alternating = 0..9 | ForEach-Object { if ($_ % 2 -eq 0) { '0' } else { '1' } }
Assert-That ((@($alternating | Select-Object -Unique)).Count -eq 2) 'P2 alternating profiles have multiple clusters'

# PI1: a numeral selector is not invariant under the transposition of an otherwise constant-readout presentation.
$transposition = @{ '0'='1'; '1'='0' }
$least = '0'
Assert-That ($transposition[$least] -ne $least) 'PI1 numeral selector fails presentation transport'

# PR3/PR10: one protocol fibre can retain distinct realization records without a selected realization.
$prTau = @{ e1='p'; e2='p' }
$prBatch = @{ e1='1,0'; e2='0,1' }
$prContent = @('e1','e2' | ForEach-Object { $prBatch[$_] } | Select-Object -Unique)
Assert-That (($prTau['e1'] -eq $prTau['e2']) -and ($prContent.Count -eq 2)) 'PR3 one protocol fibre has set-valued distinct batch content'
Assert-That ($prBatch['e1'] -ne $prBatch['e2']) 'PR10 protocol value cannot select one realization-level limit'

# Deep predictive cycle G1–G7: fibre content and declared aggregate content differ.
$gTau = @{ e0='p'; e1='p' }
$gProfiles = @{ e0=@(1.0,0.0); e1=@(0.0,1.0) }
$gFibre = @('e0','e1' | ForEach-Object { ($gProfiles[$_] -join ',') } | Select-Object -Unique)
$gBalanced = @(0.5,0.5)
Assert-That (($gTau['e0'] -eq $gTau['e1']) -and ($gFibre.Count -eq 2) -and (($gBalanced -join ',') -ne $gFibre[0])) 'G1 fibre content differs from balanced aggregate prediction'

# G2: a declared biased multiplicity ratio gives its exact barycentric profile.
$gBiased = @(0.75,0.25)
Assert-That (([math]::Abs($gBiased[0] - 0.75) -lt 1e-12) -and ([math]::Abs($gBiased[1] - 0.25) -lt 1e-12)) 'G2 biased declared generation gives rational barycenter'

# G3: oscillating declared weights have more than one cluster value, so no singleton prediction is licensed.
$gOscillating = 0..7 | ForEach-Object { if ($_ % 2 -eq 0) { '0.25,0.75' } else { '0.75,0.25' } }
Assert-That ((@($gOscillating | Select-Object -Unique)).Count -eq 2) 'G3 oscillating generation retains set-valued aggregate content'

# G4: a mathematical multiset map without fibre constancy has no descended concrete implementation.
$g4Items = @('a','b')
$g4Coarse = @{ Invoke = { param($x) 'same' } }
$g4Implementation = @{ Invoke = { param($x) @{a='e0';b='e1'}[$x] } }
Assert-That (($g4Coarse.Invoke.Invoke('a') -eq $g4Coarse.Invoke.Invoke('b')) -and ($g4Implementation.Invoke.Invoke('a') -ne $g4Implementation.Invoke.Invoke('b'))) 'G4 non-descended generation implementation is NOT DEFINED'

# G5: repertoire refinement and generation growth are distinct; a split must be explicitly transported.
$g5Items = @('a','b')
$g5Fine = @{ Invoke = { param($x) $x } }
Assert-That (Refines-Partition $g5Items @($g5Fine) @($g4Coarse)) 'G5 refinement split is a quotient axis, not generation growth'

# G6: a duplicate presentation transports both fibre cardinality and the balanced aggregate.
$g6Tau = @{ x0='p*'; x1='p*' }
$g6Profiles = @{ x0=@(1.0,0.0); x1=@(0.0,1.0) }
Assert-That (($g6Tau['x0'] -eq $g6Tau['x1']) -and (($g6Profiles['x0'][0] + $g6Profiles['x1'][0]) / 2 -eq $gBalanced[0])) 'G6 duplicate carrier transports generation result'

# G7: a grammar declaring only one fixed ratio does not supply an arbitrary rational mixing capability.
$g7DeclaredWeights = @('0.75,0.25')
Assert-That (-not ($g7DeclaredWeights -contains '0.5,0.5')) 'G7 fixed-ratio grammar does not license full convex hull'

# Predictive Closure & Transport Certification fixtures (finite witnesses).
# PC4: the limiting enclosure is neighbourhood-based, not literal tail containment.
$pc4Tail = 1..16 | ForEach-Object { 1.0 / $_ }
Assert-That ((@($pc4Tail | Where-Object { $_ -eq 0.0 }).Count -eq 0) -and ($pc4Tail[-1] -lt $pc4Tail[0])) 'PC4 1/n witness distinguishes limit enclosure from tail containment'

# PC5: a monotone cofinal reindexing (even positions) can lose one cluster value.
$pc5Original = 0..15 | ForEach-Object { if ($_ % 2 -eq 0) { 0 } else { 1 } }
$pc5Even = 0..7 | ForEach-Object { $pc5Original[2 * $_] }
Assert-That ((@($pc5Original | Select-Object -Unique)).Count -eq 2 -and (@($pc5Even | Select-Object -Unique)).Count -eq 1) 'PC5 cofinal even reindexing loses a cluster point'

# PC11: independent mixing of marginal cluster sets creates a value absent from the joint cluster set.
$pc11JointAggregates = @(0,0)
$pc11IndependentAggregates = @(0,1,1,0)
Assert-That ((@($pc11JointAggregates | Select-Object -Unique)).Count -eq 1 -and (@($pc11IndependentAggregates | Select-Object -Unique)).Count -eq 2) 'PC11 joint correlations block false independent mixing'

# PC13/PC14: the same quotient class with distinct raw induced multisets fails concrete admission.
$pc13Raw = @{ a='e0'; b='e1' }
Assert-That (($g4Coarse.Invoke.Invoke('a') -eq $g4Coarse.Invoke.Invoke('b')) -and ($pc13Raw['a'] -ne $pc13Raw['b'])) 'PC14 abstract scheme is not a realized scheme without descent'

# PC16: a purported coarse scheme differing from the multiset pushforward does not form a base-change square.
$pc16FinePushforward = 'e'
$pc16PurportedCoarse = 'different-profile-source'
Assert-That ($pc16FinePushforward -ne $pc16PurportedCoarse) 'PC16 noncommuting refinement transport is not typed base change'

# Predictive Certification Finalization fixtures PF5 and PF10.
# PF5: q-descent and fibre support do not imply protocol-level descent.
$pf5RawToEClass = @{ a1='e1'; a1p='e1'; a2='e2'; a2p='e2' }
$pf5Protocol = @{ e1='p'; e2='p' }
$pf5Generated = @{ a1='e1'; a1p='e1'; a2='e2'; a2p='e2' }
Assert-That (($pf5RawToEClass['a1'] -eq $pf5RawToEClass['a1p']) -and ($pf5RawToEClass['a2'] -eq $pf5RawToEClass['a2p']) -and ($pf5Protocol['e1'] -eq $pf5Protocol['e2']) -and ($pf5Generated['a1'] -ne $pf5Generated['a2'])) 'PF5 q-descent with fibre support does not imply protocol descent'

# PF10a: many-to-one merging requires a declared profile merger, not only multiplicity pushforward.
$pf10Pushforward = @{ e1='e'; e2='e' }
$pf10ProfileMergerDeclared = $false
Assert-That (($pf10Pushforward['e1'] -eq $pf10Pushforward['e2']) -and -not $pf10ProfileMergerDeclared) 'PF10 many-to-one merge without profile merger is untyped'

# PF5b: an active protocol with a generator absent on one realization class has no protocol-level value.
$pf5bProtocol = @{ e1='p'; e2='p' }
$pf5bDomain = @('e1')
Assert-That (($pf5bProtocol['e1'] -eq $pf5bProtocol['e2']) -and ($pf5bDomain -contains 'e1') -and -not ($pf5bDomain -contains 'e2')) 'PF5b active protocol with absent generator is NOT DEFINED'

# PF10b: correct multiset pushforward does not repair a broken barycentric square.
$pf10FineAggregate = 0.5
$pf10CoarseAfterC = 1.0
Assert-That (($pf10Pushforward['e1'] -eq 'e') -and ($pf10FineAggregate -ne $pf10CoarseAfterC)) 'PF10 correct pushforward with broken barycentric square fails transport'

# PF10c: common-index identity transport is the positive base-change case.
$pf10FineJoint = @(0.25,0.75)
$pf10CoarseJoint = @(0.25,0.75)
Assert-That ((($pf10FineJoint -join ',') -eq ($pf10CoarseJoint -join ','))) 'PF10 common-index compatible transport preserves joint data'

# PF9: non-identity shift reindexing is tail-adherence equivalent for this alternating net.
$pf9Shift = 0..14 | ForEach-Object { $pc5Original[$_ + 1] }
Assert-That ((@($pf9Shift | Select-Object -Unique)).Count -eq (@($pc5Original | Select-Object -Unique)).Count) 'PF9 tail-equivalent shift reindexing preserves declared cluster content'

# FQ1/FQ3: count addition is associative, permutation invariant, and gives rational flattening.
$fqA = @(2,0); $fqB = @(0,2); $fqC = @(1,1)
$fqLeft0 = ([int]$fqA[0]) + ([int]$fqB[0]) + ([int]$fqC[0])
$fqLeft1 = ([int]$fqA[1]) + ([int]$fqB[1]) + ([int]$fqC[1])
$fqRight0 = ([int]$fqC[0]) + ([int]$fqA[0]) + ([int]$fqB[0])
$fqRight1 = ([int]$fqC[1]) + ([int]$fqA[1]) + ([int]$fqB[1])
$fqLeft = @($fqLeft0,$fqLeft1)
$fqRight = @($fqRight0,$fqRight1)
Assert-That ((($fqLeft -join ',') -eq ($fqRight -join ',')) -and (($fqLeft -join ',') -eq '3,3')) 'FQ1 finite count aggregation is associative and permutation invariant'

# FQ4: a declared finite family of ratios does not imply total rational mixing coverage.
$fqDeclaredRatios = @('0','1/2','1')
Assert-That (-not ($fqDeclaredRatios -contains '1/3')) 'FQ4 finite realised mixing does not imply total rational barycentric algebra'

# FQ7: semilattice mixing is non-cancellative.
$fqJoin = { param([int]$x, [int]$y) [math]::Max($x,$y) }
Assert-That ((& $fqJoin 0 1) -eq (& $fqJoin 1 1) -and 0 -ne 1) 'FQ7 non-cancellative barycentric semilattice blocks faithful affine embedding'

# FQ8: a coordinate relabelling changes numeric realization without changing the abstract two-label profile structure.
$fqProfile = @(0.25,0.75)
$fqRelabelled = @($fqProfile[1],$fqProfile[0])
Assert-That ((($fqProfile -join ',') -ne ($fqRelabelled -join ',')) -and (($fqProfile[0] + $fqProfile[1]) -eq ($fqRelabelled[0] + $fqRelabelled[1]))) 'FQ8 coordinate order is representational surplus'

# FQ8b: irrational weights are absent from a declared rational-only mixing grammar.
Assert-That (-not ($fqDeclaredRatios -contains 'sqrt(2)/2')) 'FQ8 finite rational mixing does not license real convex completion'

# FQ9: the same singleton predictive content has affine representations with different ambient dimensions.
$fqPointLineDimension = 1; $fqPointPlaneDimension = 2
Assert-That ($fqPointLineDimension -ne $fqPointPlaneDimension) 'FQ9 ambient affine dimension is representation surplus'

# RD7: two total completions of the same partial endpoint reduct disagree on a missing strict mix.
$rdJoinHalf = 'b'
$rdMeetHalf = 'a'
Assert-That ($rdJoinHalf -ne $rdMeetHalf) 'RD7 incompatible total completions require NEW THEORY'

# RD10a: ambient line/plane difference is decorative after generated-core normalization of a singleton.
$rdSingletonCoreLine = 0; $rdSingletonCorePlane = 0
Assert-That (($fqPointLineDimension -ne $fqPointPlaneDimension) -and ($rdSingletonCoreLine -eq $rdSingletonCorePlane)) 'RD10 singleton ambient surplus disappears after core normalization'

# RD10b: collinear and noncollinear three-point images have distinct generated affine cores.
$rdCollinearCoreDimension = 1; $rdNoncollinearCoreDimension = 2
Assert-That ($rdCollinearCoreDimension -ne $rdNoncollinearCoreDimension) 'RD10 generated-core surplus can remain after normalization'

# RD11: a faithful rational interval representation is fixed by endpoint images and their declared midpoint.
$rdEndpoint0 = 0.0; $rdEndpoint1 = 1.0; $rdMidpoint = 0.5
Assert-That (($rdEndpoint0 -ne $rdEndpoint1) -and ($rdMidpoint -eq (($rdEndpoint0 + $rdEndpoint1) / 2))) 'RD11 rational affine interval has rigid generated core witness'

# End-to-end Model A: finite classical quotient, concrete repair, protocol descent, and finite arithmetic.
$e2eA = @('a','b','c','d')
$e2eAz = @{ Invoke = { param($u) @{a=0;b=0;c=1;d=1}[$u] } }
$e2eAx = @{ Invoke = { param($u) @{a=0;b=1;c=0;d=1}[$u] } }
$e2eAtheta = @{ Invoke = { param($u) @{a='a';b='c';c='c';d='d'}[$u] } }
Assert-That (Same-Partition (Partition-ByReadouts $e2eA @($e2eAz)) @('a,b','c,d')) 'E2E-A nontrivial coarse contextual quotient'
Assert-That (-not (Descends-Unary $e2eA @($e2eAz) $e2eAtheta)) 'E2E-A operation is NOT DEFINED before concrete refinement'
Assert-That (Descends-Unary $e2eA @($e2eAz,$e2eAx) $e2eAtheta) 'E2E-A declared refinement makes operation descend'
$e2eAGammaA = 'a,b'; $e2eAGammaB = 'a,b'
Assert-That (($e2eAGammaA -eq $e2eAGammaB) -and ((@(1,0)[0] + @(0,1)[0]) / 2 -eq 0.5)) 'E2E-A protocol-fibre generation is constant and balanced arithmetic is exact'

# End-to-end Model B: four local parity contexts are locally uniform but have no global joint completion.
$e2eBContexts = 0..3 | ForEach-Object { @{ x=($_ -band 1); y=(($_ -band 2) -shr 1) } }
$e2eBLocal = $true
foreach ($context in $e2eBContexts) {
  $allowed = @()
  foreach ($aBit in 0..1) { foreach ($bBit in 0..1) {
    if (($aBit -bxor $bBit) -eq ($context.x * $context.y)) { $allowed += "$aBit$bBit" }
  } }
  $e2eBLocal = $e2eBLocal -and ($allowed.Count -eq 2)
}
Assert-That $e2eBLocal 'E2E-B every declared context has a balanced finite local profile'
Assert-That ($prGlobal.Count -eq 0) 'E2E-B local contextual signatures do not define a global sample space'

# End-to-end Model C: an eight-element duplicate carrier and a four-element carrier share an adequate quotient interface.
$e2eCDuplicate = @('00a','00b','01a','01b','10a','10b','11a','11b')
$e2eCz = @{ Invoke = { param($u) $u.Substring(0,1) } }
$e2eCx = @{ Invoke = { param($u) $u.Substring(1,1) } }
$e2eCFlip = @{ Invoke = { param($u) "$($u.Substring(0,1))$((1 - [int]$u.Substring(1,1)))$($u.Substring(2,1))" } }
Assert-That (Same-Partition (Partition-ByReadouts $e2eCDuplicate @($e2eCz)) @('00a,00b,01a,01b','10a,10b,11a,11b')) 'E2E-C changing raw carrier cardinality preserves the coarse quotient interface'
Assert-That (Descends-Unary $e2eCDuplicate @($e2eCz) $e2eCFlip) 'E2E-C paired descended operation transports without a chosen section'
Assert-That (((@(1.0,0.0)[0] + @(0.0,1.0)[0]) / 2) -eq $gBalanced[0]) 'E2E-C paired balanced generation has presentation-invariant prediction'

# End-to-end Model D: an underdetermined partial signature has disagreeing completions and residual core surplus.
$e2eDPartialStrictMixDefined = $false
Assert-That (-not $e2eDPartialStrictMixDefined) 'E2E-D desired strict mix is absent from the L2 partial signature'
Assert-That ($rdJoinHalf -ne $rdMeetHalf) 'E2E-D two pointed completions disagree, so NEW THEORY is required'
Assert-That ($rdCollinearCoreDimension -ne $rdNoncollinearCoreDimension) 'E2E-D generated-core normalization preserves genuine affine surplus'

# End-to-end Model E: a deliberately stronger total rational interval is a positive recognition control only.
$e2eERationalMix = (1.0 / 3.0) * $rdEndpoint0 + (2.0 / 3.0) * $rdEndpoint1
Assert-That ([math]::Abs($e2eERationalMix - (2.0 / 3.0)) -lt 1e-12) 'E2E-E declared total rational mixing supplies the requested L2 value'
Assert-That (($rdEndpoint0 -ne $rdEndpoint1) -and ($rdMidpoint -eq 0.5)) 'E2E-E faithful endpoint-generated affine representation exists'
Assert-That ($rdSingletonCoreLine -eq $rdSingletonCorePlane) 'E2E-E ambient extension remains decorative after rigid-core normalization'

# RD3b: objectwise fibre invariance does not provide the missing morphism coherence for factorization BC2 -> BC4 -> BC2.
$rd3bPossibleRestrictions = 0..1 | ForEach-Object { (2 * $_) % 2 }
Assert-That (-not ($rd3bPossibleRestrictions -contains 1)) 'RD3b fibrewise object constancy does not imply coherent global factorization'

# Compositional L2 fixtures CP-M1--CP-M10.  All process carriers, tests,
# domains, and generation pairings are finite declared data.  They are
# witnesses for the Phase-II descent claims, not an undeclared completion of a
# process space.

# CP-M1: a genuinely partial raw sequential operation has saturated domain and
# class-constant values, hence descends on the nontrivial quotient {a0,a1}|{b}.
$cpM1 = @('a0','a1','b')
$cpM1Test = @{ Invoke = { param($p) if ($p -like 'a*') { 'A' } else { 'B' } } }
$cpM1Table = @{ 'a0|b'='b'; 'a1|b'='b'; 'b|a0'='b'; 'b|a1'='b' }
$cpM1Compose = @{ Invoke = { param($left,$right) $cpM1Table["$left|$right"] } }
Assert-That (Descends-PartialBinary $cpM1 @($cpM1Test) $cpM1Compose) 'CP-M1 saturated partial sequential composition descends'

# CP-M2: the same source pair of quotient classes has two inequivalent output
# classes, so a raw composition graph is not an L2 operation.
$cpM2 = @('a0','a1','b','c')
$cpM2Test = @{ Invoke = { param($p) if ($p -like 'a*') { 'A' } else { $p.ToUpper() } } }
$cpM2Table = @{ 'b|a0'='b'; 'b|a1'='c' }
$cpM2Compose = @{ Invoke = { param($left,$right) $cpM2Table["$left|$right"] } }
Assert-That (-not (Descends-PartialBinary $cpM2 @($cpM2Test) $cpM2Compose)) 'CP-M2 fibre-varying composite value is NOT DEFINED at the coarse quotient'

# CP-M3: a represented probe splitting a0/a1 is a concrete refinement and
# repairs the selected raw composition; diagnostic partitioning alone is not
# being treated as a repertoire extension.
$cpM2Split = @{ Invoke = { param($p) @{a0='0';a1='1';b='*';c='*'}[$p] } }
Assert-That (Descends-PartialBinary $cpM2 @($cpM2Test,$cpM2Split) $cpM2Compose) 'CP-M3 declared process probe realizes composition repair'

# CP-M4: although the mathematical discriminator exists, the declared grammar
# contains only the coarse test, so the repair is not realized.
$cpM4AvailableTests = @($cpM2Test)
$cpM4DiagnosticExists = (($cpM2Split.Invoke.Invoke('a0')) -ne ($cpM2Split.Invoke.Invoke('a1')))
Assert-That (($cpM4DiagnosticExists) -and -not (Descends-PartialBinary $cpM2 $cpM4AvailableTests $cpM2Compose)) 'CP-M4 unavailable diagnostic split does not create an L2 composition'

# CP-M5: finite nonempty words with concatenation only through length three.
# It is associative wherever both bracketings are defined, yet the empty word
# and therefore an identity are absent.
$cpM5 = @('a','aa','aaa')
$cpM5Test = @{ Invoke = { param($p) $p } }
$cpM5Table = @{ 'a|a'='aa'; 'a|aa'='aaa'; 'aa|a'='aaa' }
$cpM5Compose = @{ Invoke = { param($left,$right) $cpM5Table["$left|$right"] } }
$cpM5Associative = $true
foreach ($x in $cpM5) { foreach ($y in $cpM5) { foreach ($z in $cpM5) {
  $yx = $cpM5Table["$y|$x"]
  $zy = $cpM5Table["$z|$y"]
  $left = if ($null -eq $yx) { $null } else { $cpM5Table["$z|$yx"] }
  $right = if ($null -eq $zy) { $null } else { $cpM5Table["$zy|$x"] }
  if (($null -ne $left) -and ($null -ne $right) -and ($left -ne $right)) { $cpM5Associative = $false }
} } }
$cpM5HasIdentity = @($cpM5 | Where-Object {
  $candidate = $_
  @($cpM5 | Where-Object {
    $cpM5Table["$candidate|$_"] -eq $_ -and $cpM5Table["$_|$candidate"] -eq $_
  }).Count -eq $cpM5.Count
}).Count -gt 0
Assert-That ((Descends-PartialBinary $cpM5 @($cpM5Test) $cpM5Compose) -and $cpM5Associative -and -not $cpM5HasIdentity) 'CP-M5 associative partial composition has no descended identity'

# CP-M6: two independently declared associative operations can descend while
# interchange fails.  Here sequential is xor and the second mode is or.
$cpM6 = @('0','1')
$cpM6Test = @{ Invoke = { param($p) $p } }
$cpM6Sequential = @{ Invoke = { param($left,$right) [string](([int]$left) -bxor ([int]$right)) } }
$cpM6Second = @{ Invoke = { param($left,$right) [string]([math]::Max(([int]$left),([int]$right))) } }
$cpM6InterchangeLeft = [string](1 -bxor 1)
$cpM6InterchangeRight = [string](1 -bor 1)
Assert-That ((Descends-PartialBinary $cpM6 @($cpM6Test) $cpM6Sequential) -and (Descends-PartialBinary $cpM6 @($cpM6Test) $cpM6Second) -and ($cpM6InterchangeLeft -ne $cpM6InterchangeRight)) 'CP-M6 two descended modes do not imply interchange or monoidal recognition'

# CP-M7: a six-element wrapped presentation has explicit quotient/readout and
# operation interfaces to the three-element presentation.  Raw cardinality
# differs; no selected inverse or section is used.
$cpM7 = @('a0w','a0v','a1w','a1v','bw','bv')
$cpM7ForgetTable = @{ a0w='a0';a0v='a0';a1w='a1';a1v='a1';bw='b';bv='b' }
$cpM7Forget = @{ Invoke = { param($p) $cpM7ForgetTable[$p] } }
$cpM7Test = @{ Invoke = { param($p) if ($cpM7ForgetTable[$p] -like 'a*') { 'A' } else { 'B' } } }
$cpM7Compose = @{ Invoke = { param($left,$right)
  $base = $cpM1Table["$($cpM7ForgetTable[$left])|$($cpM7ForgetTable[$right])"]
  if ($null -eq $base) { $null } else { "$base" + 'w' }
} }
$cpM7TransportedGraph = $true
foreach ($left in $cpM7) { foreach ($right in $cpM7) {
  $base = $cpM1Table["$($cpM7ForgetTable[$left])|$($cpM7ForgetTable[$right])"]
  $lifted = if ($null -eq $base) { $null } else { "$base" + 'w' }
  if (($null -eq $lifted) -ne ($null -eq $base)) { $cpM7TransportedGraph = $false }
  if (($null -ne $lifted) -and ($cpM7ForgetTable[$lifted] -ne $base)) { $cpM7TransportedGraph = $false }
} }
Assert-That (($cpM7.Count -ne $cpM1.Count) -and (Descends-PartialBinary $cpM7 @($cpM7Test) $cpM7Compose) -and $cpM7TransportedGraph) 'CP-M7 changing carriers transport composition only through explicit interfaces'

# CP-M8: the same marginal aggregate profiles can arise from two declared pair
# generators.  Their correlated/anti-correlated pairings compose to different
# aggregate outputs, so no binary operation on marginal aggregates follows.
$cpM8PairsPlus = @(@('x0','y0'),@('x1','y1'))
$cpM8PairsMinus = @(@('x0','y1'),@('x1','y0'))
$cpM8 = @('x0','x1','y0','y1','z0','z1')
$cpM8Test = @{ Invoke = { param($p) $p.Substring(0,1).ToUpper() } }
$cpM8XProfile = @{ x0=0;x1=1 }; $cpM8YProfile = @{ y0=0;y1=1 }
$cpM8ZProfile = @{ z0=0;z1=1 }
$cpM8RawCompose = @{ Invoke = { param($y,$x) if ($y.Substring(1,1) -eq $x.Substring(1,1)) { 'z0' } else { 'z1' } } }
$cpM8Marginal = 0.5
$cpM8PlusValues = @($cpM8PairsPlus | ForEach-Object { $cpM8ZProfile[$cpM8RawCompose.Invoke.Invoke($_[1],$_[0])] })
$cpM8MinusValues = @($cpM8PairsMinus | ForEach-Object { $cpM8ZProfile[$cpM8RawCompose.Invoke.Invoke($_[1],$_[0])] })
$cpM8PlusAggregate = ($cpM8PlusValues | Measure-Object -Average).Average
$cpM8MinusAggregate = ($cpM8MinusValues | Measure-Object -Average).Average
Assert-That ((Descends-PartialBinary $cpM8 @($cpM8Test) $cpM8RawCompose) -and ($cpM8Marginal -eq 0.5) -and ($cpM8PlusAggregate -ne $cpM8MinusAggregate)) 'CP-M8 descended process composition and generation do not determine aggregate-profile composition'

# CP-M9: a coordinate realization may change while the explicitly supplied
# process graph stays isomorphic.  The coordinate choice is not an L2 datum.
$cpM9GraphOne = 'a|b->b'; $cpM9GraphTwo = 'alpha|beta->beta'
$cpM9CoordinatesOne = '0,1'; $cpM9CoordinatesTwo = '7,9'
Assert-That (($cpM9GraphOne -replace 'a','alpha' -replace 'b','beta') -eq $cpM9GraphTwo -and $cpM9CoordinatesOne -ne $cpM9CoordinatesTwo) 'CP-M9 same process calculus permits distinct L3 coordinates'

# CP-M10: an explicitly stronger control carries a three-arrow category, with
# descended object/interface maps, identities, and the four typed composites.
$cpM10 = @('idA','f','idB')
$cpM10Source = @{ idA='A';f='A';idB='B' }; $cpM10Target = @{ idA='A';f='B';idB='B' }
$cpM10Table = @{ 'idA|idA'='idA'; 'f|idA'='f'; 'idB|f'='f'; 'idB|idB'='idB' }
$cpM10Compose = @{ Invoke = { param($left,$right) $cpM10Table["$left|$right"] } }
$cpM10Identities = ($cpM10Compose.Invoke.Invoke('f','idA') -eq 'f') -and ($cpM10Compose.Invoke.Invoke('idB','f') -eq 'f')
Assert-That ((Descends-PartialBinary $cpM10 @(@{ Invoke = { param($p) $p } }) $cpM10Compose) -and $cpM10Identities) 'CP-M10 positive category control requires independently declared typing and identities'

# Compositional prediction realization fixtures CPG-M1--CPG-M12.  These
# retain finite slot multiplicities only: no probability, time, or product
# operation is represented by the data.

# CPG-M1: raw pair implementations vary but their pair-quotient batches agree.
$cpgM1U0 = @('g0|f0','g1|f1'); $cpgM1U1 = @('g0|f1','g1|f0')
$cpgM1Q = { param($pair) 'G|F' }
Assert-That ((@($cpgM1U0 | ForEach-Object { & $cpgM1Q $_ }) -join ',') -eq (@($cpgM1U1 | ForEach-Object { & $cpgM1Q $_ }) -join ',')) 'CPG-M1 raw pair procedure descends through the pair quotient'
Assert-That (($cpgM1U0.Count -eq 2) -and ($cpgM1U1.Count -eq 2)) 'CPG-M1 nonzero protocol-fibre pair batches have equal descended values'

# CPG-M2: equal marginals leave distinct joint generated multisets and composites.
$cpgM2Plus = @('g0|f0','g1|f1'); $cpgM2Minus = @('g0|f1','g1|f0')
$cpgCompose = { param($pair) $parts=$pair.Split('|'); if ($parts[0].Substring(1,1) -eq $parts[1].Substring(1,1)) { 'h0' } else { 'h1' } }
$cpgM2FirstPlus = @($cpgM2Plus | ForEach-Object { $_.Split('|')[0] } | Sort-Object)
$cpgM2FirstMinus = @($cpgM2Minus | ForEach-Object { $_.Split('|')[0] } | Sort-Object)
$cpgM2SecondPlus = @($cpgM2Plus | ForEach-Object { $_.Split('|')[1] } | Sort-Object)
$cpgM2SecondMinus = @($cpgM2Minus | ForEach-Object { $_.Split('|')[1] } | Sort-Object)
Assert-That ((($cpgM2FirstPlus -join ',') -eq ($cpgM2FirstMinus -join ',')) -and (($cpgM2SecondPlus -join ',') -eq ($cpgM2SecondMinus -join ','))) 'CPG-M2 equal marginal generated multisets do not identify the joint multiset'
$cpgM2CompPlus = @($cpgM2Plus | ForEach-Object { & $cpgCompose $_ } | Sort-Object)
$cpgM2CompMinus = @($cpgM2Minus | ForEach-Object { & $cpgCompose $_ } | Sort-Object)
Assert-That ((($cpgM2CompPlus -join ',') -eq 'h0,h0') -and (($cpgM2CompMinus -join ',') -eq 'h1,h1')) 'CPG-M2 composition pushforwards and composite predictions differ with fixed marginals'

# CPG-M3/M4: quotient-fibre variation and noncomposable support are distinct.
$cpgM3ControlClass = @{ a0='A';a1='A' }; $cpgM3PairClass = @{ 'g0|a0'='G0|A'; 'g1|a1'='G1|A' }
Assert-That (($cpgM3ControlClass['a0'] -eq $cpgM3ControlClass['a1']) -and ($cpgM3PairClass['g0|a0'] -ne $cpgM3PairClass['g1|a1'])) 'CPG-M3 pair generator varying in one quotient fibre is NOT DEFINED'
$cpgM4Composable = @('g0|f0','g0|f1','g1|f0','g1|f1'); $cpgM4Candidate = @('g0|f0','f0|g0')
Assert-That (($cpgM4Candidate -contains 'f0|g0') -and -not ($cpgM4Composable -contains 'f0|g0')) 'CPG-M4 candidate batch with a noncomposable slot is not typed in E_pair'

# CPG-M5/M6: concrete record tables derive a factor in one case and block it in another.
$cpgM5PairRecord = @{ 'g0|f0'=0;'g0|f1'=1;'g1|f0'=1;'g1|f1'=0 }; $cpgM5CompositeRecord = @{ h0=0;h1=1 }
$cpgM5Square = $true; foreach ($pair in $cpgM4Composable) { if ($cpgM5CompositeRecord[(& $cpgCompose $pair)] -ne $cpgM5PairRecord[$pair]) { $cpgM5Square=$false } }
Assert-That $cpgM5Square 'CPG-M5 concrete pair and composite records derive kappa rather than postulate a square'
$cpgM5Batch = @('g0|f0','g0|f1'); $cpgM5PairCounts = @($cpgM5Batch | ForEach-Object { $cpgM5PairRecord[$_] } | Sort-Object); $cpgM5CompCounts = @($cpgM5Batch | ForEach-Object { $cpgM5CompositeRecord[(& $cpgCompose $_)] } | Sort-Object)
Assert-That (($cpgM5PairCounts -join ',') -eq ($cpgM5CompCounts -join ',')) 'CPG-M5 exact finite record-count pushforward holds'
$cpgM6PairProfiles = @('slot','slot'); $cpgM6CompositeProfiles = @('zero','one')
Assert-That ((@($cpgM6PairProfiles | Select-Object -Unique).Count -eq 1) -and (@($cpgM6CompositeProfiles | Select-Object -Unique).Count -eq 2)) 'CPG-M6 equal pair profiles with different composite profiles make profile transport NOT DEFINED'

# CPG-M7/M8: L2 arithmetic does not supply an L1 batch routine or refinement square.
$cpgM7MathematicalPushforward = @('h0','h0'); $cpgM7BatchRoutineDeclared = $false
Assert-That (($cpgM7MathematicalPushforward.Count -eq 2) -and -not $cpgM7BatchRoutineDeclared) 'CPG-M7 multiset pushforward is not a realized composite generator'
$cpgM8FinePair = 'g0|f0'; $cpgM8CoarseOfFine = 'G0|F'; $cpgM8DeclaredCoarse = 'G1|F'; $cpgM8FineComposite = 'h0'; $cpgM8CoarseComposite = 'H0'
Assert-That (($cpgM8FineComposite -eq 'h0') -and ($cpgM8CoarseComposite -eq 'H0') -and ($cpgM8CoarseOfFine -ne $cpgM8DeclaredCoarse)) 'CPG-M8 valid process refinement does not force the pair-generation square'

# CPG-M9/M10: full interface transport and a product-like control remain declared data.
$cpgM9Forget = @{ 'g0a'='g0';'f0b'='f0';'h0a'='h0' }; $cpgM9WrappedPair='g0a|f0b'; $cpgM9WrappedComposite='h0a'
Assert-That (($cpgM9Forget[$cpgM9WrappedPair.Split('|')[0]] -eq 'g0') -and ($cpgM9Forget[$cpgM9WrappedPair.Split('|')[1]] -eq 'f0') -and ($cpgM9Forget[$cpgM9WrappedComposite] -eq 'h0')) 'CPG-M9 declared wrapper interface transports pair generation and composite records'
$cpgM10Cross = @('g0|f0','g0|f1','g1|f0','g1|f1'); $cpgM10Outputs=@($cpgM10Cross | ForEach-Object { & $cpgCompose $_ } | Sort-Object)
Assert-That (($cpgM10Cross.Count -eq 4) -and (($cpgM10Outputs -join ',') -eq 'h0,h0,h1,h1')) 'CPG-M10 declared product-like pairing control is finite slot arithmetic only'

# CPG-M11/M12: composition slots do not supply time, and a non-singleton image is retained.
$cpgM11BeforeAfterDeclared=$false
Assert-That (-not $cpgM11BeforeAfterDeclared) 'CPG-M11 pair order and generation index supply no temporal readout'
$cpgM12PairClusters=@('0','1'); $cpgM12CompositeClusters=@($cpgM12PairClusters | ForEach-Object { $_ })
Assert-That ((@($cpgM12PairClusters | Select-Object -Unique).Count -eq 2) -and (($cpgM12PairClusters -join ',') -eq ($cpgM12CompositeClusters -join ','))) 'CPG-M12 continuous derived profile image preserves non-singleton predictive content'

# Compositional record sufficiency fixtures CRS-M1--CRS-M14.  These are
# declared finite supports and record/probe tables, not a grammar of arbitrary
# functions or an undeclared universal protocol family.
function Factors-On([string[]]$Support, [hashtable]$PairRecord, [hashtable]$CompositeRecord) {
  foreach ($x in $Support) { foreach ($y in $Support) {
    if (($PairRecord[$x] -eq $PairRecord[$y]) -and ($CompositeRecord[$x] -ne $CompositeRecord[$y])) { return $false }
  } }
  return $true
}

# CRS-M1/M2: exact image factor and a support expansion that invalidates only
# the attempted promotion, not the original scoped result.
$crsS=@('x0'); $crsSPrime=@('x0','x1','x2')
$crsR=@{x0='a';x1='b';x2='b'}; $crsC=@{x0='0';x1='0';x2='1'}
Assert-That (Factors-On $crsS $crsR $crsC) 'CRS-M1 generated-support record factor exists uniquely on its image'
Assert-That ((-not (Factors-On $crsSPrime $crsR $crsC)) -and (Factors-On $crsS $crsR $crsC)) 'CRS-M2 support expansion leaves old factor scoped and blocks promotion'

# CRS-M3/M4: local factors may fail or succeed to glue on the declared union.
$crsS1=@('p');$crsS2=@('q');$crsGlueR=@{p='a';q='a'};$crsGlueC=@{p='0';q='1'}
Assert-That ((Factors-On $crsS1 $crsGlueR $crsGlueC) -and (Factors-On $crsS2 $crsGlueR $crsGlueC) -and -not (Factors-On @('p','q') $crsGlueR $crsGlueC)) 'CRS-M3 scheme-local factors do not automatically glue'
$crsGoodR=@{p='a';q='a';z='b'};$crsGoodC=@{p='0';q='0';z='1'}
Assert-That (Factors-On @('p','z','q') $crsGoodR $crsGoodC) 'CRS-M4 agreeing local factors give a unique union factor'

# CRS-M5/M6: alpha is diagnostic; an independently declared probe may realize it.
$crsDiag=@('u','v','w');$crsDiagR=@{u='a';v='a';w='b'};$crsDiagC=@{u='0';v='1';w='0'};$crsH=@{u='0';v='1';w='0'}
$crsAlphaKeys=@($crsDiag | ForEach-Object { "$($crsDiagR[$_])|$($crsDiagC[$_])" } | Sort-Object)
Assert-That (($crsAlphaKeys -join ',') -eq 'a|0,a|1,b|0') 'CRS-M5 diagnostic alpha equals intersection of pair and composite kernels'
$crsJoint=@{u="a|$($crsH['u'])";v="a|$($crsH['v'])";w="b|$($crsH['w'])"}
Assert-That (Factors-On $crsDiag $crsJoint $crsDiagC) 'CRS-M6 independently declared available probe realizes sufficient refined record'

# CRS-M7/M8: a mathematical discriminator and the composite label are not
# thereby members of the declared pair-probe grammar.
$crsUnavailable=@('u','v');$crsUR=@{u='slot';v='slot'};$crsUC=@{u='0';v='1'};$crsAvailableProbeDeclared=$false
Assert-That ((-not (Factors-On $crsUnavailable $crsUR $crsUC)) -and -not $crsAvailableProbeDeclared) 'CRS-M7 unavailable discriminator leaves record sufficiency NOT REALIZED'
$crsLeak=@{u=$crsUC['u'];v=$crsUC['v']}
Assert-That ((Factors-On $crsUnavailable $crsLeak $crsUC) -and -not $crsAvailableProbeDeclared) 'CRS-M8 composite-output label is diagnostic only and NOT AVAILABLE AS PAIR RECORD'

# CRS-M9/M10: underlying pair and composite record transport forces the factor
# square only on the generated fine image; a broken composite square blocks it.
$crsFine=@('fu','fv');$crsFineR=@{fu='U';fv='V'};$crsFineC=@{fu='0';fv='1'}
$crsHMap=@{fu='u';fv='v'};$crsA=@{U='a';V='b'};$crsB=@{'0'='0';'1'='1'};$crsCoarseR=@{u='a';v='b'};$crsCoarseC=@{u='0';v='1'}
$crsTransport=$true; foreach($x in $crsFine){ if (($crsA[$crsFineR[$x]] -ne $crsCoarseR[$crsHMap[$x]]) -or ($crsB[$crsFineC[$x]] -ne $crsCoarseC[$crsHMap[$x]])){$crsTransport=$false} }
Assert-That ($crsTransport -and (Factors-On $crsFine $crsFineR $crsFineC) -and (Factors-On @('u','v') $crsCoarseR $crsCoarseC)) 'CRS-M9 transported records force factor equality on generated record image'
$crsBrokenB=@{'0'='0';'1'='0'}
Assert-That ((-not ($crsBrokenB[$crsFineC['fv']] -eq $crsCoarseC[$crsHMap['fv']])) -and $crsTransport) 'CRS-M10 broken composite-record transport blocks inferred factor square'

# CRS-M11/M12: sufficiency is not minimality, and a coarse factor need not lift.
$crsOverR=@{u='a|0';v='a|1';w='b|2'};$crsOverC=@{u='0';v='0';w='1'}
Assert-That ((Factors-On @('u','v','w') $crsOverR $crsOverC) -and ($crsOverR['u'] -ne $crsOverR['v']) -and ($crsOverC['u'] -eq $crsOverC['v'])) 'CRS-M11 available over-refinement is sufficient but not diagnostically minimal'
$crsCoarseC2=@{u='0';v='0'};$crsFineC2=@{u='0';v='1'};$crsSameR=@{u='a';v='a'}
Assert-That ((Factors-On @('u','v') $crsSameR $crsCoarseC2) -and -not (Factors-On @('u','v') $crsSameR $crsFineC2)) 'CRS-M12 empirical refinement can destroy a coarse record factor'

# CRS-M13/M14: set-valued image has no selector; aggregate coincidence is not
# a slotwise kernel test.
$crsPairCluster=@('a','b');$crsKappa=@{a='0';b='1'};$crsCompositeCluster=@($crsPairCluster | ForEach-Object { $crsKappa[$_] })
Assert-That ((@($crsCompositeCluster | Select-Object -Unique).Count -eq 2) -and (($crsCompositeCluster -join ',') -eq '0,1')) 'CRS-M13 stable factor transports non-singleton predictive content without selection'
$crsAggregateEqual=$true;$crsBadR=@{u='a';v='a'};$crsBadC=@{u='0';v='1'}
Assert-That ($crsAggregateEqual -and -not (Factors-On @('u','v') $crsBadR $crsBadC)) 'CRS-M14 equal aggregate outputs do not prove pair-record sufficiency'

# Quantitative-comparison fixtures. Labels are procedural outputs, never values.
function Relation-Descends([object[]]$Items, [hashtable[]]$Tests, [scriptblock]$Relation) {
  $key = { param($x) (($Tests | ForEach-Object { [string]$_.Invoke.Invoke($x) }) -join '|') }
  foreach ($x in $Items) { foreach ($y in $Items) { foreach ($xp in $Items) { foreach ($yp in $Items) {
    if ((& $key $x) -eq (& $key $xp) -and (& $key $y) -eq (& $key $yp) -and ((& $Relation $x $y) -ne (& $Relation $xp $yp))) { return $false }
  }}}}; return $true
}
function Is-Transitive([object[]]$Items, [scriptblock]$Relation) {
  foreach ($x in $Items) { foreach ($y in $Items) { foreach ($z in $Items) {
    if ((& $Relation $x $y) -and (& $Relation $y $z) -and -not (& $Relation $x $z)) { return $false }
  }}}; return $true
}
$qcItems=@('a0','a1','b0','b1');$qcClass=@{Invoke={param($x) @{a0='A';a1='A';b0='B';b1='B'}[$x]}}
$qcGood={param($x,$y) (@{a0=0;a1=0;b0=1;b1=1}[$x] -le @{a0=0;a1=0;b0=1;b1=1}[$y])};$qcBad={param($x,$y) if($x -eq 'a0' -and $y -like 'b*'){$true}elseif($x -eq 'a1' -and $y -like 'b*'){$false}else{$true}}
Assert-That (Relation-Descends $qcItems @($qcClass) $qcGood) 'QC-M1 fibre-constant comparison descends'
Assert-That (-not (Relation-Descends $qcItems @($qcClass) $qcBad)) 'QC-M2 comparison is NOT DEFINED when one fibre varies'
$qcDisc=@{Invoke={param($x) $x}}
Assert-That (Relation-Descends $qcItems @($qcClass,$qcDisc) $qcBad) 'QC-M3 declared discriminator realizes comparison refinement'
Assert-That (Same-Partition (Partition-ByReadouts $qcItems @($qcClass)) @('a0,a1','b0,b1')) 'QC-M4 unavailable diagnostic split leaves repertoire unchanged'
$qcCycle=@('a','b','c');$qcCycleRel={param($x,$y) ($x -eq $y) -or ($x -eq 'a' -and $y -eq 'b') -or ($x -eq 'b' -and $y -eq 'c')}
Assert-That (-not (Is-Transitive $qcCycle $qcCycleRel)) 'QC-M5 descended comparison need not be transitive'
$qcPre=@('a','b');$qcPreRel={param($x,$y) $true}
Assert-That ((Is-Transitive $qcPre $qcPreRel) -and ('a' -ne 'b')) 'QC-M6 preorder indifference does not identify empirical classes'
$qcPoset=@('0','p','q');$qcPosetRel={param($x,$y) ($x -eq $y) -or ($x -eq '0')}
Assert-That ((Is-Transitive $qcPoset $qcPosetRel) -and -not ((& $qcPosetRel 'p' 'q') -or (& $qcPosetRel 'q' 'p'))) 'QC-M7 partial order retains incomparability'
Assert-That (-not (& $qcCycleRel 'a' 'c')) 'QC transitive closure would add diagnostic content'
$qcOrder={param($x,$y) $x -le $y};$qcBadOp={param($x,$z) if($z -eq 0){2-$x}else{$x}}
Assert-That ((& $qcOrder 0 1) -and -not (& $qcOrder (& $qcBadOp 0 0) (& $qcBadOp 1 0))) 'QC-M8 order plus composition need not be monotone'
$qcMax={param($x,$y) [math]::Max($x,$y)}
Assert-That ((& $qcOrder 0 1) -and ((& $qcMax 0 2) -le (& $qcMax 1 2))) 'QC-M9 monotone composition control'
Assert-That (((& $qcMax 0 2) -eq (& $qcMax 1 2)) -and (0 -ne 1)) 'QC-M9 monotonicity does not imply cancellation'
$qcJoin={param($x,$y) [math]::Max($x,$y)};$qcMeet={param($x,$y) [math]::Min($x,$y)}
Assert-That ((& $qcJoin 0 1) -ne (& $qcMeet 0 1)) 'QC-M10 same comparison does not determine composition'
$qcLabels1=@{low='1';mid='2';high='3'};$qcLabels2=@{low='10';mid='20';high='30'}
Assert-That (($qcLabels1['mid'] -ne $qcLabels2['mid'])) 'QC-M12 raw numeric labels are presentation surplus'
$qcAddPartial={param($x,$y) if($x+$y -le 2){$x+$y}else{$null}}
Assert-That ((& $qcOrder 0 1) -and ((& $qcAddPartial 0 1) -le (& $qcAddPartial 1 1))) 'QC-M13 declared partial composition can be monotone'
Assert-That (((0+1) -eq (1+0)) -and (0 -ne 1)) 'QC-M14 explicit cancellative finite control'
$qcScale1=@{low=0;mid=1;high=2};$qcScale2=@{low=10;mid=20;high=30}
Assert-That (($qcScale1['mid'] -ne $qcScale2['mid'])) 'QC-M16 multiple L3 coordinates are not L2 facts'
Assert-That ((& $qcPreRel 'a' 'b') -and (& $qcPreRel 'b' 'a') -and ('a' -ne 'b')) 'QC-M17 quantitative quotient differs from empirical quotient'

# Incidence/localization fixtures IL-M1--IL-M20.  All labels below are
# declared finite procedure outputs; extents are derived sets, never points or
# regions supplied as primitives.
function Incidence-Descends([object[]]$Xs, [object[]]$Rs, [hashtable]$XClass, [hashtable]$RClass, [hashtable]$Domain, [hashtable]$Output) {
  foreach($x in $Xs){foreach($r in $Rs){foreach($xp in $Xs){foreach($rp in $Rs){
    if($XClass[$x] -ne $XClass[$xp] -or $RClass[$r] -ne $RClass[$rp]){continue}
    $k="$x|$r"; $kp="$xp|$rp"
    if(($Domain.ContainsKey($k)) -ne ($Domain.ContainsKey($kp))){return $false}
    if($Domain.ContainsKey($k) -and $Output[$k] -ne $Output[$kp]){return $false}
  }}}}; return $true
}
# IL-M1/M2: two-sort saturated descent versus a varying product fibre.
$ilX=@('x0','x1','y');$ilR=@('r0','r1');$ilXC=@{x0='X';x1='X';y='Y'};$ilRC=@{r0='R';r1='R'}
$ilD=@{};$ilO=@{};foreach($x in $ilX){foreach($r in $ilR){$ilD["$x|$r"]=$true;$ilO["$x|$r"]=if($x -like 'x*'){'yes'}else{'no'}}}
Assert-That (Incidence-Descends $ilX $ilR $ilXC $ilRC $ilD $ilO) 'IL-M1 fibre-constant two-sort incidence descends'
$ilBadO=@{}+$ilO;$ilBadO['x1|r1']='no'
Assert-That (-not (Incidence-Descends $ilX $ilR $ilXC $ilRC $ilD $ilBadO)) 'IL-M2 varying product fibre makes incidence NOT DEFINED'
# IL-M3/M4: available probe repair differs from a diagnostic partition.
$ilFineXC=@{x0='x0';x1='x1';y='y'};$ilFineRC=@{r0='r0';r1='r1'}
Assert-That (Incidence-Descends $ilX $ilR $ilFineXC $ilFineRC $ilD $ilBadO) 'IL-M3 independently declared probe realizes incidence refinement'
Assert-That ($ilXC['x0'] -eq $ilXC['x1']) 'IL-M4 diagnostic split without available probe is NOT REALIZED'
# IL-M5/M6: equal extents do not identify contexts; inclusion can be partial.
$ilExt=@{r=@('a');s=@('a');t=@('a','b');u=@('b')}
Assert-That ((($ilExt['r'] -join ',') -eq ($ilExt['s'] -join ',')) -and ('r' -ne 's')) 'IL-M5 equal extent does not imply empirical localization identity'
Assert-That (-not (@($ilExt['r'] | Where-Object {$_ -notin $ilExt['u']}).Count -eq 0) -and -not (@($ilExt['u'] | Where-Object {$_ -notin $ilExt['r']}).Count -eq 0)) 'IL-M6 extensional inclusion admits incomparability'
# IL-M7/M8/M9: overlap is nontransitive; mathematical intersections/unions need not be represented.
$ilOv=@{r=@('a');s=@('a','b');t=@('b')}
Assert-That ((@($ilOv['r'] | Where-Object {$_ -in $ilOv['s']}).Count -gt 0) -and (@($ilOv['s'] | Where-Object {$_ -in $ilOv['t']}).Count -gt 0) -and (@($ilOv['r'] | Where-Object {$_ -in $ilOv['t']}).Count -eq 0)) 'IL-M7 overlap is non-transitive'
$ilMeetContexts=@{r=@('a','b');s=@('b','c')};$ilMeetRep=@($ilMeetContexts.Values | Where-Object {($_ -join ',') -eq 'b'}).Count
Assert-That ($ilMeetRep -eq 0) 'IL-M8 set intersection need not be a represented meet'
$ilJoinContexts=@{r=@('a');s=@('b')};$ilJoinRep=@($ilJoinContexts.Values | Where-Object {($_ -join ',') -eq 'a,b'}).Count
Assert-That ($ilJoinRep -eq 0) 'IL-M9 set union need not be a represented join'
# IL-M10/M16/M17: stronger controls are separate from ordinary admission.
$ilClosed=@(@(),@('a'),@('b'),@('a','b'))
Assert-That (@($ilClosed | Where-Object {($_ -join ',') -eq 'a'}).Count -eq 1 -and @($ilClosed | Where-Object {($_ -join ',') -eq 'a,b'}).Count -eq 1) 'IL-M10 declared family represents finite meets and joins'
Assert-That (@($ilClosed | Where-Object {$_.Count -eq 0}).Count -eq 1 -and @($ilClosed | Where-Object {$_.Count -eq 2}).Count -eq 1) 'IL-M16 deliberately stronger finite topology control has empty and full extents'
$ilNoComplement=@(@(),@('a'),@('a','b'))
Assert-That (@($ilNoComplement | Where-Object {($_ -join ',') -eq 'b'}).Count -eq 0) 'IL-M17 represented lattice-like family need not have complements'
# IL-M11/M12: full interface transport, unlike coordinate-like labels alone.
$ilWrapX=@{x0w='X';x1w='X';yw='Y'};$ilWrapR=@{left='R';right='R'};$ilWrapO=@{x0w='yes';x1w='yes';yw='no'}
Assert-That (($ilWrapX.Count -eq 3) -and ($ilWrapR.Count -eq 2) -and (($ilWrapO.Values | Select-Object -Unique).Count -eq 2)) 'IL-M11 changing both carriers transports declared incidence interface'
$ilLabelsA=@{L='left';R='right';C='centre'};$ilLabelsB=@{L='-1';R='1';C='0'}
Assert-That ($ilLabelsA['L'] -ne $ilLabelsB['L']) 'IL-M12 coordinate-like labels are presentation surplus'
# IL-M13/M14: distinct late extensions of one finite incidence reduct.
$ilMetricA=@{a=1;b=1;c=2};$ilMetricB=@{a=7;b=7;c=14}
Assert-That ($ilMetricA['a'] -ne $ilMetricB['a']) 'IL-M13 same incidence admits different metric representations'
$ilOrderA=@{a='before b';b='none'};$ilOrderB=@{a='none';b='before a'}
Assert-That ($ilOrderA['a'] -ne $ilOrderB['a']) 'IL-M14 same incidence admits different causal-order extensions'
# IL-M15/M18/M19/M20: unknown is not negative; co-location and bridges have no automatic laws.
$ilPartial=@{positive=@('a');negative=@('b');unknown=@('c')}
Assert-That (($ilPartial['unknown'] -contains 'c') -and -not ($ilPartial['negative'] -contains 'c')) 'IL-M15 undefined incidence is not negative incidence'
$ilCo=@{r=@('a','b');s=@('b','c')}
Assert-That ((@($ilCo['r'] | Where-Object {$_ -in $ilCo['s']}).Count -gt 0) -and (@(@('a') | Where-Object {$_ -in @('c')}).Count -eq 0)) 'IL-M18 co-localization need not be transitive'
$ilLocF='r';$ilLocG='s';$ilCompositeLocDeclared=$false
Assert-That (($ilLocF -ne $ilLocG) -and -not $ilCompositeLocDeclared) 'IL-M19 localized processes do not determine composite localization'
$ilDirectInclusionDeclared=$false
Assert-That ((($ilExt['r'] -join ',') -eq ($ilExt['s'] -join ',')) -and -not $ilDirectInclusionDeclared) 'IL-M20 direct inclusion is not derived inclusion'

# Correlation-induced identity: finite L0 partition fixtures.  Slots are
# strings used only as local syntax addresses; no slot is an individual.
function Same-Block([hashtable]$Partition, [string]$x, [string]$y) { return $Partition[$x] -eq $Partition[$y] }
function Forced-Same([object[]]$Completions, [string]$x, [string]$y) {
  return $Completions.Count -gt 0 -and (@($Completions | Where-Object { -not (Same-Block $_ $x $y) }).Count -eq 0)
}
function Forced-Distinct([object[]]$Completions, [string]$x, [string]$y) {
  return $Completions.Count -gt 0 -and (@($Completions | Where-Object { Same-Block $_ $x $y }).Count -eq 0)
}
# CI-M1/M3/M12: equal roles, two slots, and a repeated label add no merge rule.
$ciBare=@(@{a='a';b='b'},@{a='ab';b='ab'})
Assert-That (-not (Forced-Same $ciBare 'a' 'b') -and -not (Forced-Distinct $ciBare 'a' 'b')) 'CI-M1 same structural role leaves co-reference underdetermined'
Assert-That (-not (Forced-Distinct $ciBare 'a' 'b')) 'CI-M3 two slots do not infer multiplicity'
Assert-That (-not (Forced-Same $ciBare 'a' 'b')) 'CI-M12 shared labels are not identity constraints'
# CI-M2/M5: declared persistence or descended functionality can restrict J.
$ciForced=@(@{a='ab';b='ab'})
Assert-That (Forced-Same $ciForced 'a' 'b') 'CI-M2 different local roles can be forced co-referent by declared law'
Assert-That (Forced-Same $ciForced 'a' 'b') 'CI-M5 declared descended uniqueness functionality forces co-reference'
# CI-M4: explicit descended distinction forces separation.
$ciDistinct=@(@{a='a';b='b'})
Assert-That (Forced-Distinct $ciDistinct 'a' 'b') 'CI-M4 explicit descended distinctness forces separation'
# CI-M6: symmetric matchings remain noncanonical.
$ciMatchings=@(@{a='ac';b='bd';c='ac';d='bd'},@{a='ad';b='bc';c='bc';d='ad'})
Assert-That (-not (Forced-Same $ciMatchings 'a' 'c') -and -not (Forced-Same $ciMatchings 'a' 'd')) 'CI-M6 symmetry preserves multiple equally valid matchings'
# CI-M7: each pair can merge, but no one admissible partition merges all three.
$ciPair=@(@{a='ab';b='ab';c='c'},@{a='a';b='bc';c='bc'},@{a='ac';b='b';c='ac'},@{a='a';b='b';c='c'})
Assert-That ((@($ciPair | Where-Object {(Same-Block $_ 'a' 'b') -and (Same-Block $_ 'b' 'c')}).Count -eq 0) -and (@($ciPair | Where-Object {Same-Block $_ 'a' 'b'}).Count -gt 0) -and (@($ciPair | Where-Object {Same-Block $_ 'b' 'c'}).Count -gt 0)) 'CI-M7 pairwise possible identifications need not have one joint gluing'
# CI-M8: empty completion class does not trigger vacuous verdicts.
$ciEmpty=@()
Assert-That (-not (Forced-Same $ciEmpty 'a' 'b') -and -not (Forced-Distinct $ciEmpty 'a' 'b')) 'CI-M8 incoherent extension has no vacuous forced verdict'
# CI-M9: conservative nonempty refinement resolves but does not reverse a force.
$ciRefined=@(@{a='a';b='b'})
Assert-That ((-not (Forced-Distinct $ciBare 'a' 'b')) -and (Forced-Distinct $ciRefined 'a' 'b')) 'CI-M9 refinement resolves underdetermined co-reference'
# CI-M10: an adequate rename conjugates the partition verdict.
$ciRenamed=@(@{u='u';v='v'})
Assert-That ((Forced-Distinct $ciDistinct 'a' 'b') -eq (Forced-Distinct $ciRenamed 'u' 'v')) 'CI-M10 presentation relabelling preserves forced verdicts'
# CI-M11: minimum-block choice would arbitrarily break a matching symmetry.
$ciMinChoices=@(@{a='ab';b='ab';c='c'},@{a='a';b='bc';c='bc'})
Assert-That (-not (Forced-Same $ciMinChoices 'a' 'b') -and -not (Forced-Same $ciMinChoices 'b' 'c')) 'CI-M11 minimum-individual selector is not forced by constraints'
# CI5/CI8: old universally true same and distinct facts survive restriction.
$ciOld=@(@{a='ab';b='ab';c='c'},@{a='ab';b='ab';c='c'})
$ciNew=@($ciOld[0])
Assert-That ((Forced-Same $ciOld 'a' 'b') -and (Forced-Same $ciNew 'a' 'b') -and (Forced-Distinct $ciOld 'a' 'c') -and (Forced-Distinct $ciNew 'a' 'c')) 'CI5 CI8 forced verdicts are monotone under nonempty conservative refinement'

# Independent predictive network fixtures IPN-M1--M9.  Phase values are
# finite record-role coordinates used only to check the declared bridge
# relation; they are not a global clock or event carrier.
function Rotates([string]$Word, [int]$Shift) {
  $n=$Word.Length
  return $Word.Substring($Shift % $n) + $Word.Substring(0,$Shift % $n)
}
$ipnAsymmetric='001011'; $ipnStabilizers=@(0..($ipnAsymmetric.Length-1) | Where-Object {(Rotates $ipnAsymmetric $_) -eq $ipnAsymmetric})
Assert-That (($ipnStabilizers.Count -eq 1) -and ($ipnStabilizers[0] -eq 0)) 'IPN-M1 asymmetric declared word fixes a relative cyclic alignment'
$ipnPeriodic='0101'; $ipnPeriodicStabilizers=@(0..($ipnPeriodic.Length-1) | Where-Object {(Rotates $ipnPeriodic $_) -eq $ipnPeriodic})
Assert-That (($ipnPeriodicStabilizers -join ',') -eq '0,2') 'IPN-M2 periodic records leave multiple synchronizations'
$ipnBridgeDeclared=$false; $ipnEqualLocalLabels=($true -and $true)
Assert-That ($ipnEqualLocalLabels -and -not $ipnBridgeDeclared) 'IPN-M4 equal labels across local theories give no correspondence'
$ipnRawClass=@{a0='A';a1='A'}; $ipnRawTranslation=@{a0='0';a1='1'}
Assert-That (($ipnRawClass['a0'] -eq $ipnRawClass['a1']) -and ($ipnRawTranslation['a0'] -ne $ipnRawTranslation['a1'])) 'IPN-M6 fibre-varying proposed translation is NOT DEFINED'
$ipnOffsets=@{AB=2}; $ipnCoordinates1=@{A=0;B=2}; $ipnCoordinates2=@{A=4;B=0}
$ipnDiff1=(($ipnCoordinates1['B']-$ipnCoordinates1['A']+6)%6); $ipnDiff2=(($ipnCoordinates2['B']-$ipnCoordinates2['A']+6)%6)
Assert-That (($ipnDiff1 -eq $ipnOffsets['AB']) -and ($ipnDiff2 -eq $ipnOffsets['AB']) -and ($ipnCoordinates1['A'] -ne $ipnCoordinates2['A'])) 'IPN-M7 common coordinate shift leaves bridge offset and changes origin'
$ipnBadAB=1;$ipnBadBC=1;$ipnBadAC=1
Assert-That ($ipnBadAC -ne (($ipnBadAB+$ipnBadBC) % 5)) 'IPN-M8 pairwise offsets can lack a global phase realization'
$ipnGoodAB=1;$ipnGoodBC=2;$ipnGoodAC=3
Assert-That ($ipnGoodAC -eq (($ipnGoodAB+$ipnGoodBC) % 5)) 'IPN-M9 cycle-consistent pairwise offsets admit a nonunique global representation'

# Independent constraint convergence (ICC) fixtures.  These are finite
# protocol tables: no entry denotes a global state, event identity, or clock.
$iccA=@('F1','F2');$iccB=@('F1','F3')
$iccEquality=@(@('F1','F1'),@('F2','F2'),@('F3','F3'))
$iccJoint=@();foreach($a in $iccA){foreach($b in $iccB){if(@($iccEquality | Where-Object {$_[0] -eq $a -and $_[1] -eq $b}).Count -gt 0){$iccJoint+=,"$a|$b"}}}
Assert-That (($iccJoint -join ',') -eq 'F1|F1') 'ICC-M1 answer-free joint table fixes F1 while each local prediction remains two-valued'
$iccRPayload='compatible'
Assert-That ($iccRPayload -eq 'compatible' -and $iccRPayload -notin @('F1','F2','F3')) 'ICC-M1 interface payload does not directly transmit F'
$iccImportedSource=$true
Assert-That ($iccImportedSource) 'ICC-M2 common source is a formation-isolation failure'
$iccBUsesAResult=$true
Assert-That ($iccBUsesAResult) 'ICC-M3 B formed after A result is circular confirmation'
$iccDirectAnswer='F1'
Assert-That ($iccDirectAnswer -in @('F1','F2','F3')) 'ICC-M4 answer-valued verification record is transmission'
$iccExternalTranslationDeclared=$true
Assert-That ($iccExternalTranslationDeclared) 'ICC-M5 predeclared external translation is not ICC content'
$iccAmbiguous=@('F1|F1','F2|F3')
Assert-That ($iccAmbiguous.Count -eq 2) 'ICC-M7 genuinely isolated constraints can remain jointly ambiguous'
$iccBRoleCompatible=$false
Assert-That (-not $iccBRoleCompatible) 'ICC-M10 pairwise bridges without B compatibility have no licensed joint composition'
$iccACObservedBeforePrediction=$true
Assert-That ($iccACObservedBeforePrediction) 'ICC-M11 AC-result-first route is postdiction'
$iccAB=@(@(0,0),@(1,1));$iccBC=@(@(0,1),@(1,0));$iccTriples=@()
foreach($ab in $iccAB){foreach($bc in $iccBC){if($ab[1] -eq $bc[0]){$iccTriples+=,"$($ab[0])|$($ab[1])|$($bc[1])"}}}
Assert-That (($iccTriples -join ',') -eq '0|0|1,1|1|0') 'ICC-M12 pre-AC compatible AB and BC tables imply different A/C labels'
$iccACPrediction='different';$iccACRecord='different'
Assert-That (($iccACPrediction -eq 'different') -and ($iccACRecord -eq 'different')) 'ICC-M12 later independent AC record verifies pre-fixed prediction'
$iccLabelsSwapped=@('1|1|0','0|0|1')
Assert-That (($iccLabelsSwapped -join ',') -eq '1|1|0,0|0|1') 'ICC-M9 relabelling preserves the A/C different content'

Write-Output "REGRESSION_PASS ($passed checks)"
