from collections import Counter

class Solution(object):
    def list_to_dict(self,lst):
        count_dict = {}
        for item in lst:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        return dict(sorted(count_dict.items()))
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        sorted_dict = dict(sorted(dict(Counter(hand)).items())) # convert list into dictionary
        sorted_dict = self.list_to_dict(hand)
        while(sorted_dict):
            first_key = next(iter(sorted_dict))
            # sorted_dict.pop(first_key)
            for key in range(first_key, first_key + groupSize):
                if sorted_dict.get(key):
                    sorted_dict[key] -= 1
                    if sorted_dict[key] == 0:
                        sorted_dict.pop(key)
                else:
                    return False
        return True






if __name__ == '__main__':
    # hand = [1,2,3,6,2,3,4,7,8]
    # hand = [1,2,3,1,2,3]
    hand = [8,6,5,7,9]

    # groupSize = 3
    groupSize = 5
    sol = Solution()
    print(sol.isNStraightHand(hand,groupSize))