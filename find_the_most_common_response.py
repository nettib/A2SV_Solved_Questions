class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response_track = {}

        for day in responses:
            for response in set(day):
                if response not in response_track:
                    response_track[response] = 1
                else:
                    response_track[response] += 1
        
        max_response = None

        for response in response_track.keys():
            if not max_response or response_track[response] > response_track[max_response]:
                max_response = response
            elif response_track[max_response] == response_track[response]:
                max_response = min(max_response, response)
        
        return max_response
        
