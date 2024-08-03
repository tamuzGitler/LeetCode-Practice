class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        for paired_domain in cpdomains:
            temp = paired_domain.split()
            visits, domain = int(temp[0]), temp[1].split(".")
            while domain:
                key = ".".join(domain)
                d[key] = d.get(key, 0) + visits
                domain.pop(0)
        ans = []
        for key, value in d.items():
            ans.append(f"{value} {key}")
        return ans


if __name__ == '__main__':
    s = "900 google.mail.com"
    a = s.split()
    print(a[1].split("."))
    sol = Solution()
    cpdomains = ["9001 discuss.leetcode.com", "100 com"]
    print(sol.subdomainVisits(cpdomains))
