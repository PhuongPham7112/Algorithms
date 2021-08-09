# source: https://www.codechef.com/LRNDSA02/problems/STFOOD
def ChefFood(N, foods):
    stores = [foods[i][0] for i in range(N)]
    people = [foods[i][1] for i in range(N)]
    prices = [foods[i][2] for i in range(N)]
    received_customers = [people[i]//(stores[i] + 1) for i in range(len(people))]
    received_profit = max([received_customers[i]*prices[i] for i in range(len(received_customers))])
    return received_profit

