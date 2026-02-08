class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_track = {}

        for cpdomain in cpdomains:
            visit, domain = cpdomain.split(" ")
            visit = int(visit)

            idx = []

            for i in range(len(domain)):
                if domain[i] == '.':
                    idx.append(i)
                
            domain_track[domain] = domain_track.get(domain, 0) + visit

            for i in idx:
                domain_track[domain[i + 1:]] = domain_track.get(domain[i + 1:], 0) + visit
        
        ans = []

        for domain in domain_track:
            ans.append(str(domain_track[domain]) + ' ' + domain)
        
        return ans
                
