from pydantic import BaseModel

class hepsiburada(BaseModel):
    memory: float
    ram: float
    screen_size: float
    power:float
    front_camera:float
    rc1:float
    rc3:float
    rc5:float
    rc7:float

    class Config:
        schema_extra = {
            "example": {
                "memory": 230.1,
                "ram": 37.8,
                "screen_size": 69.2,
                "power":5000.0,
                "front_camera":20.0,
                "rc1":4.0,
                "rc3":16.0,
                "rc5":2.0,
                "rc7":0.0,

            }
        }
