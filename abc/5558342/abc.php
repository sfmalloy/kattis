<?php

function swap(& $arr, $a, $b) {
  $temp = $arr[$a];
  $arr[$a] = $arr[$b];
  $arr[$b] = $temp;
}

$nums = explode(" ", trim(fgets(STDIN)));

// Median of 3 sort
if ($nums[2] < $nums[0])
  swap($nums, 2, 0);
if ($nums[2] < $nums[1])
  swap($nums, 2, 1);
if ($nums[1] < $nums[0])
  swap($nums, 1, 0);

$letters_in = fgets(STDIN);
$abc = "ABC";
$map = array();
for ($i = 0; $i < 3; ++$i)
  $map[$abc[$i]] = $nums[$i];

for ($i = 0; $i < 3; ++$i)
  echo $map[$letters_in[$i]] . " ";
