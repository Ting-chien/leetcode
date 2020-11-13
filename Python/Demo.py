class ThreeSum:

    def solution1(self, nums):

        mapOfNums = [[value, index] for index, value in enumerate(nums)]
        mapOfNums.sort()

        lhs_pointer = 0
        rhs_pointer = len(nums) - 1

        result = []

        while lhs_pointer < rhs_pointer:
            
            twoSum = mapOfNums[lhs_pointer][0] + mapOfNums[rhs_pointer][0]
            target = 0 - (mapOfNums[lhs_pointer][0] + mapOfNums[rhs_pointer][0])
            # print([mapOfNums[lhs_pointer][0], target, mapOfNums[rhs_pointer][0]])
            if target in (item[0] for item in mapOfNums[lhs_pointer+1:rhs_pointer]) and [mapOfNums[lhs_pointer][0], target, mapOfNums[rhs_pointer][0]] not in result:
                result.append([mapOfNums[lhs_pointer][0], target, mapOfNums[rhs_pointer][0]])
            
            if twoSum > 0:
                rhs_pointer -= 1
            elif twoSum < 0:
                lhs_pointer += 1
            elif twoSum == 0:
                if mapOfNums[lhs_pointer+1][0] < 0:
                    lhs_pointer += 1
                    continue
                elif mapOfNums[rhs_pointer-1][0] > 0:
                    rhs_pointer -= 1
                    continue
                else:
                    return result

        return result

if __name__ == "__main__":
    question = ThreeSum()
    print(question.solution1([1,2,-2,-1]))
