class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        d={1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
         10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16: 'Sixteen',
         17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
         60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}
        res=""
        ans=self.solve(num,d,res)
        return " ".join(ans.split())
    
    def solve(self,num,d,res):
        if num==0:
            return res
        elif num<20:
            res+=d[num]
            return res
        elif 20<=num<100:
            res+=d[(num//10)*10]+" "+self.solve(num%10,d,res)
            return res
        elif 100<=num<1000:
            res+=d[(num//100)]+ " " +d[100]+" "+self.solve(num%100,d,res)
            return res
        elif 1000<=num<1000000:
            res+=self.solve(num//1000,d,res)+" "+d[1000]+" "+self.solve(num%1000,d,res)
            return res
        elif 1000000<=num<1000000000:
            res+=self.solve(num//1000000,d,res)+ " " + d[1000000] +" "+self.solve(num%1000000,d,res)
            return res
        else:
            res+=self.solve(num//1000000000,d,res)+" "+d[1000000000]+" "+self.solve(num%1000000000,d,res)
            return res
        