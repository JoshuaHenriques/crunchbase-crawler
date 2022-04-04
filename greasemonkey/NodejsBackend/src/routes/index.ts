import { Router } from "express"
import { experts } from "./experts/experts"


const route = Router()

route.post("/experts", experts)

export default route