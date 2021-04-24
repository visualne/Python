'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [2,3,5,7], target = 7,
A solution set is:
[
  [2,2,3]
  [2,5]
  [7]
]


Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

target = 7
input_candidates = [2,3,5,7]

summed_up_values_equaling_target = []

for index in range(len(input_candidates)-1):
    current_value = input_candidates[index]

    if current_value + sum(summed_up_values_equaling_target) < target:
        summed_up_values_equaling_target.append(current_value)

    if sum(summed_up_values_equaling_target) == target:
        print summed_up_values_equaling_target


