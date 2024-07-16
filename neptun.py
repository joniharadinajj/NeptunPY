# shtetet = {
#     "Kosova" : {
#         "Kryeqyteti" : "Prishtina",
#         "Popullsia" : 1500541
#     },
#     "Albania" : {
#         "Kryeqyteti" : "Tirana",
#         "Popullsia" : 3520568
#     },
#     "Maqedonia e Veriut" : {
#         "Kryeqyteti" : "Shkupi",
#         "Popullsia" : 1850103
#     }
# }
# print(shtetet["Albania"]["Kryeqyteti"])

produktet = {
    "tv" : 450,
    "mouse" : 7,
    "laptop": 1000,
    "keyboard" : 50
}
print(sorted(produktet.values()))
cmimivogel = min(produktet.values())
print(f"produkti me cmimin me te vogel eshte {cmimivogel} ")