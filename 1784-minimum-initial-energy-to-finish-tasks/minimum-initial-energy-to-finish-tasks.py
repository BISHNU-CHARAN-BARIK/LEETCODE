class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        energy=0
        res=0
        for ele in tasks:
            if(energy < ele[1]):
                extra=ele[1]-energy
                res+=extra
                energy+=extra
            energy-=ele[0]
        return res