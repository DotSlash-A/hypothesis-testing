from fastapi import FastAPI
from pydantic import BaseModel
from scipy import stats

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Request body model
class TestData(BaseModel):
    testType: str
    data1: list[float]
    data2: list[float] = None

@app.post("/test")
def run_test(data: TestData):
    test_type = data.testType

    result = {}

    if test_type == "ttest_ind":
        # Independent t-test
        t_stat, p_value = stats.ttest_ind(data.data1, data.data2)
        result["ho"] = "The means of the two groups are equal."
        result["h1"] = "The means of the two groups are not equal."
    elif test_type == "ttest_rel":
        # Paired t-test
        t_stat, p_value = stats.ttest_rel(data.data1, data.data2)
        result["ho"] = "The paired samples have the same means."
        result["h1"] = "The paired samples have different means."
    elif test_type == "anova":
        # One-Way ANOVA
        f_stat, p_value = stats.f_oneway(data.data1, data.data2)
        result["ho"] = "All group means are equal."
        result["h1"] = "At least one group mean is different."
    else:
        return {"error": "Test type not supported"}

    result["p_value"] = p_value
    result["conclusion"] = "Reject Ho" if p_value < 0.05 else "Fail to reject Ho"
    return result




