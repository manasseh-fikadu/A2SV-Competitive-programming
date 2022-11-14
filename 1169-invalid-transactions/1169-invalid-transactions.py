class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = {} 
        result = set()
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            if name not in store:
                store[name] = []
                if int(amount) > 1000:
                    result.add(i)
            else:
                prevTrans = store[name]
                for j in range(len(prevTrans)):
                    pname, ptime, pamount, pcity = transactions[prevTrans[j]].split(",")
                    if int(amount) > 1000:
                        result.add(i)
                        
                    if abs(int(time) - int(ptime)) <= 60 and city != pcity:
                        result.add(i)
                        result.add(prevTrans[j])
            store[name].append(i)
		
        return [transactions[t] for t in result]