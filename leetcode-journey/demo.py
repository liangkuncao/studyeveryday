from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            parts = domain.split(',')
            for i in range(len(parts) - 1, -1, -1):
                domain_count[','.join(parts[i:])] += int(count)
        return [str(count) + ' ' + domain for domain, count in domain_count.items()]


print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))