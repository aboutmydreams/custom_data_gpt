import requests


def get_import_data(keyword):
    base_url = "https://api.uktradeinfo.com/Commodity"
    query_params = {
        "$filter": f"Hs6Description eq '{keyword}'",
        "$expand": "Imports($expand=Trader)",
    }

    response = requests.get(base_url, params=query_params)
    data = response.json()
    print(data)

    import_data = []
    for commodity in data["value"]:
        for imp in commodity["Imports"]:
            trader_name = imp["Trader"]["TraderName"]
            import_value = imp["Value"]
            import_data.append({"TraderName": trader_name, "ImportValue": import_value})

    return import_data


# 您可以将上述代码保存为一个Python文件，并在需要的地方调用`get_import_data`函数来获取特定商品的进口数据。例如，如果您想获取关键词为"汽车"的商品进口数据，可以使用以下代码：


import_data = get_import_data("wrench")
for imp in import_data:
    print(f"公司名称：{imp['TraderName']}，进口数据：{imp['ImportValue']}")
