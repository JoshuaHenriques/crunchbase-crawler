import { Router } from "express"
import { insertExperts } from "./endpoints/insertExperts"
import { getExperts } from "./endpoints/getExperts"
import { getCompanies } from "./endpoints/getCompanies"


const route = Router()

route.post("/insertExperts", insertExperts)

route.get("/getExperts", getExperts)

route.get("/getCompanies", getCompanies)

export default route