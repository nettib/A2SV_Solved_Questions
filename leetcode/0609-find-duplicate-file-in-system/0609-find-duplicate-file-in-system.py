class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        track = {}

        for i in range(len(paths)):
            path = paths[i].split()
            d = path[0]
            path = path[1:]
            for f in path:
                c = f.split('(')
                fil = d + "/" + c[0]
                content = c[-1][:-1]
                if content not in track:
                    track[content] = []
                track[content].append(fil)
        
        ans = []
        for key in track.keys():
            if len(track[key]) > 1:
                ans.append(track[key])
        
        return ans