from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Risk Data (from your document)
risk_data = {
    "Water Supply Projects": {
        "Green Field": ["LOA. (To know the date & year when the project was awarded)","Source of Water."  "Details of wet works, Sum Insured towards it.","Cost bifurcation of the project. (Intake, Pipe line, other structures) ",
"Details of pipe line (length, diameter).","Details of pipeline crossing water body, sum insured towards it. (To check wet risk exposure)","Methodology of pipeline laying, Appx Length (Ex: Open trench, HDD, jacking method, micro tunneling).","Storage practices.","Index Map/ Block Diagram / Blocks or districts covered (To check exposure)"
],
        "Brown Field": ["Details of Dismantling works if any, Sum Insured towards it.","Details of Pipe Line as mentioned above","Detailed scope of works"
]
    },
    "Sewerage Treatment Plant Projects": {
        "Green Field": ["LOA", "Cost bifurcation of the project", "Location of the project (Latitude, Longitude)"],
        "Brown Field": ["Details of Dismantling works if any, Sum Insured towards it.", "Fire protection details at site", "Cost bifurcation of the project"]
    },
    "Road Projects":{
        "Green Field": ["LOA", "KMZ file.", "Details of wet works, Sum Insured towards it."],
          "Brown Field": ["LOA","Details of wet works, Sum Insured towards it."]
    },
    "Residential and Commercial Projects":{
        "Normal":["Project Configuration- No of basements, No of floors, No of towers, interconnection.", "Layout.", "Location details (Latitude, Longitude)." ,"Type of Building RCC / Steel structure ","Storage Practices"],
        "If more than 3 basements":["Geotechnical report.","Type of foundation.","Details of Slope protection Works"]
        },
    "Road or Metro Project Involving Tunnel Construction":{
        "Normal":["LOA.","Cross sectional detail of tunnel." ,"Construction methodology.","Geotechnical report and rock layer along with tunnel profile.",
"Details of joint / fault falling in tunnel profile.","Contractor’s previous experience in tunnel construction.","Soil / rock description at both portal area with max and min overburden across tunnel profile.",
"Min and Max distance between LHS and RHS tunnel along with nos. of cross passage and their cross-sectional detail.",
"Technical schedule A,B,C,D and H of project along with TCS details.","KMZ File."]
    },
    "Canal  Projects" :{
        "Normal":["LOA.","Index Map.","Details of wet works, Sum Insured towards it.","Cost Bifurcation of the project."]
    },
    "Irrigation Projects":{
        "Normal":["LOA.","Details of wet works, Sum Insured towards it.","Details of pipe line (length, diameter).","Details of pipeline crossing water body, sum insured towards it.", 
"Methodology of pipeline laying (Ex: Open trench, HDD, jacking method, micro tunneling).","Storage practices.","Index Map."
]
    },
    "Jetty Projects/ Water Front Structures":{
       "Normal" :["Sum Insured towards temporary works.","Construction Methodology.","Storage Practices.","Cost Bifurcation of the Project." ]
    },

    "Elevated Metro Projects":{
        "Normal":["LOA.","Index Map."]
    },

    "Bullet Train Projects":{
        "Normal":["KMZ File.", "LOA.", "Details of wet works, Sum Insured towards it.", "Storage Practices.","Construction Methodology."]
    },

    "Manufacturing Unit":{
        "Normal":["Layout.","Type of Building RCC / Steel structure.", "Height of Building.","Cost Bifurcation of the project.","Location details (Latitude, Longitude).","Duration of the project.",
"Contractor details"
]
    }






    # Add more categories from your document
}

class UserInput(BaseModel):
    category: str
    subcategory: str | None = None

@app.post("/get-risk-details")
async def get_risk_details(input: UserInput):
    category = input.category
    subcategory = input.subcategory
    
    if category in risk_data:
        if subcategory and subcategory in risk_data[category]:
            return {"details": risk_data[category][subcategory]}
        return {"details": list(risk_data[category].keys())}
    
    return {"error": "Category not found"}
