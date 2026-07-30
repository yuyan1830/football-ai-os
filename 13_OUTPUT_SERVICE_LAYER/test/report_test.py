import sys


sys.path.insert(
    0,
    r"E:\football_v\13_OUTPUT_SERVICE_LAYER"
)


from report_service import ReportService



service = ReportService()



data = {


"match":
{
"home":"Manchester City",
"away":"Liverpool"
},


"model_result":
{
"home_win_probability":0.42,
"draw_probability":0.2225,
"away_win_probability":0.3575
},


"decision":
{
"decision":"主胜",
"confidence":0.42
}


}



result = service.generate(
    data
)


print("==============================")
print("OUTPUT SERVICE TEST")
print("==============================")


print(result)

