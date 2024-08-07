from collections import defaultdict


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        duplicateFiles = []
        contentDict = defaultdict(list)
        for path in paths:
            files = path.split(" ")
            root = files[0] + "/"
            for i in range(1, len(files)):
                temp = files[i].split("(")
                content = temp[1][:-1]
                contentDict[content].append(root + temp[0])
        for values in contentDict.values():
            if len(values) > 1:
                duplicateFiles.append(values)
        return duplicateFiles


if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    sol = Solution()
    print(sol.findDuplicate(paths))
