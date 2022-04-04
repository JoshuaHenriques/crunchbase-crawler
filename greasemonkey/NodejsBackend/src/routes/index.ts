import { Router } from "express"
import { insertExperts } from "./endpoints/insertExperts"
import { getExperts } from "./endpoints/getExperts"


const route = Router()

route.post("/experts", insertExperts)

route.get("/company", getExperts)

export default route