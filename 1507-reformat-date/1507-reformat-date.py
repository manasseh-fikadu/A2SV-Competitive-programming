class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        new_date = date.split(" ")
        if len(new_date[0]) == 4:
            date_val = new_date[0][:2]
        else:
            date_val = new_date[0][:1]
            
        month = str(months.index(new_date[1]) + 1 )
        if len(month) == 1:
            month = '0' + month
        if len(date_val) == 1:
            date_val = '0' + date_val
            
        return new_date[2] + "-" + month + "-" + date_val