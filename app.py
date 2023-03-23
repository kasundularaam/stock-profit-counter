def getTransactions():
    transactions = []
    keyPress = "y"
    while keyPress == "y":
        day, x, y = list(
            map(int, input("Enter day, num of shares and price: ").split()))
        transactions.append({"day": day, "x": x, "y": y})
        keyPress = input(
            "If You need to add more transactions enter (y) or else enter (n): ")
    return transactions


def validateTransactions(buying, selling):
    buyingStocksCount = 0
    sellingStocksCount = 0
    for bStock in buying:
        buyingStocksCount += bStock["x"]
    for sStock in selling:
        sellingStocksCount += sStock["x"]
    if (sellingStocksCount > buyingStocksCount):
        return False
    return True


def getProfitAndUpdatedBTransactions(sTransaction, bTransactions):
    totalStockProfit = 0
    sStockCount = sTransaction["x"]
    updatedBTransactions = bTransactions.copy()
    for i in range(len(bTransactions)):
        singleStockProfit = sTransaction["y"] - bTransactions[i]["y"]

        rest = bTransactions[i]["x"] - sStockCount

        if (rest > 0):
            updatedBTransactions[i-(len(bTransactions) -
                                    len(updatedBTransactions))]["x"] = rest
        else:
            updatedBTransactions.pop(i-(len(bTransactions) -
                                        len(updatedBTransactions)))

        if (rest >= 0):
            totalStockProfit += singleStockProfit*sStockCount
            break

        totalStockProfit += singleStockProfit*bTransactions[i]["x"]
        sStockCount -= bTransactions[i]["x"]

    return {"updatedBTransactions": updatedBTransactions, "totalStockProfit": totalStockProfit}


print("\n~BUYING TRANSACTIONS~\n")

buyingTransactions = getTransactions()

print("\n~SELLING TRANSACTIONS~\n")

sellingTransactions = getTransactions()

validationResult = validateTransactions(
    buyingTransactions, sellingTransactions)

if (validationResult == False):
    print("ERROR: Your transactions are not valid please try again!")
    exit()

print("\n~PROFIT~\n")


updatedBTransactions = buyingTransactions.copy()

finalProfit = 0

for sellingTransaction in sellingTransactions:
    profitAndUpdatedBTransactions = getProfitAndUpdatedBTransactions(
        sellingTransaction, updatedBTransactions)
    updatedBTransactions = profitAndUpdatedBTransactions["updatedBTransactions"]
    finalProfit += profitAndUpdatedBTransactions["totalStockProfit"]

print(f"${finalProfit}")
