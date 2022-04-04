// let company = "google"
// let companyUUID = "6acfa7da-1dbd-936e-d985-cf07a1b27711"
// let company = "farmart"
// let companyUUID = "c30e2e2c-2873-ef6f-c5f1-a2874f20f66f"
let company = "amazon"
let companyUUID = "05554f65-6aa9-4dd1-6271-8ce2d60f10c4"
let expertsList = []

const pushToExpertList = (data) => {
    data.entities.forEach((expert) => {
        expertsList.push({
            name: expert.properties.name,
            jobTitle: expert.related_entities["contact_item.has_contact_item.forward"].entities[0].properties.job_title,
            jobDepartments: expert.properties.job_departments,
            linkedIn: expert.properties.linkedin
        })
    })
}

const downloadExpertList = () => {
    let dataString = JSON.stringify(expertsList, undefined, 4)

    var blob = new Blob([dataString], {
        type: 'text/json'
    }),
        e = document.createEvent('MouseEvents'),
        a = document.createElement('a')

    a.download = "experts.json"
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}

const sendToDB = async () => {
    const res = await fetch('http://localhost:4000/experts', {
				method: "POST",
				body: JSON.stringify({
                    company: {
                        id: companyUUID,
                        name: company,
                    },
					experts: expertsList
				}),
				headers: {
				"Content-type": "application/json"
				},
	})
}

const fetchTheRest = async (last, cnt) => {
    for (let i = 0; i < cnt + 1; i++) {
        let fetchData = await fetch("https://www.crunchbase.com/v4/data/searches/contacts?source=profile-contacts-card", {
            "credentials": "include",
            "headers": {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
                "X-Requested-With": "XMLHttpRequest",
                "X-XSRF-TOKEN": "qedaymbRRqCX8coeRH7B6sALeShDWHFUEP0IHNWU6Nc",
                "Content-Type": "application/json",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1"
            },
            "referrer": `https://www.crunchbase.com/organization/${company}/people`,
            "body": `{\"collection_id\":\"contacts\",\"field_ids\":[\"name\",\"linkedin\",\"job_levels\",\"job_departments\",\"private_work_emails\",\"private_personal_emails\",\"private_work_phones\",\"private_personal_phones\"],\"query\":[{\"type\":\"predicate\",\"field_id\":\"organization\",\"operator_id\":\"includes\",\"values\":[\"${companyUUID}\"]},{\"type\":\"predicate\",\"field_id\":\"num_contact_items\",\"operator_id\":\"gte\",\"values\":[1]},{\"type\":\"predicate\",\"field_id\":\"job_departments\",\"operator_id\":\"includes\",\"values\":[\"finance\"]}],\"limit\":10,\"order\":[{\"field_id\":\"job_priority\",\"sort\":\"desc\"},{\"field_id\":\"identifier\",\"sort\":\"asc\"}],\"related_entities\":[{\"collection_id\":\"contact_item.has_contact_item.forward\",\"field_ids\":[\"identifier\",\"hashes\",\"job_title\",\"source_type\"],\"limit\":10},{\"collection_id\":\"private_contact_item.has_private_contact_item.forward\",\"field_ids\":[\"identifier\",\"hashes\",\"work_emails\",\"personal_emails\",\"work_phones\",\"personal_phones\",\"source_type\"],\"limit\":10}],\"after_id\":\"${last}\"}`,
            "method": "POST",
            "mode": "cors"
        })
        let data = await fetchData.json()
        last = data.entities[9].uuid
        console.log(last)
        pushToExpertList(data)
    }
}

const grabExperts = async () => {
    let fetchData = await fetch("https://www.crunchbase.com/v4/data/searches/contacts?source=profile-contacts-card", {
        "credentials": "include",
        "headers": {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "X-Requested-With": "XMLHttpRequest",
            "X-XSRF-TOKEN": "qedaymbRRqCX8coeRH7B6sALeShDWHFUEP0IHNWU6Nc",
            "Content-Type": "application/json",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1"
        },
        "referrer": `https://www.crunchbase.com/organization/${company}/people`,
        "body": `{\"collection_id\":\"contacts\",\"field_ids\":[\"name\",\"linkedin\",\"job_levels\",\"job_departments\",\"private_work_emails\",\"private_personal_emails\",\"private_work_phones\",\"private_personal_phones\"],\"query\":[{\"type\":\"predicate\",\"field_id\":\"organization\",\"operator_id\":\"includes\",\"values\":[\"${companyUUID}\"]},{\"type\":\"predicate\",\"field_id\":\"num_contact_items\",\"operator_id\":\"gte\",\"values\":[1]},{\"type\":\"predicate\",\"field_id\":\"job_departments\",\"operator_id\":\"includes\",\"values\":[\"finance\"]}],\"limit\":10,\"order\":[{\"field_id\":\"job_priority\",\"sort\":\"desc\"},{\"field_id\":\"identifier\",\"sort\":\"asc\"}],\"related_entities\":[{\"collection_id\":\"contact_item.has_contact_item.forward\",\"field_ids\":[\"identifier\",\"hashes\",\"job_title\",\"source_type\"],\"limit\":10},{\"collection_id\":\"private_contact_item.has_private_contact_item.forward\",\"field_ids\":[\"identifier\",\"hashes\",\"work_emails\",\"personal_emails\",\"work_phones\",\"personal_phones\",\"source_type\"],\"limit\":10}]}`,
        "method": "POST",
        "mode": "cors"
    })

    // make checks to see if less than 10 experts
    let data = await fetchData.json()
    let lastPersonID = data.entities[9].uuid
    let loopCnt = data.count / 10
    pushToExpertList(data)

    await fetchTheRest(lastPersonID, loopCnt)
}

grabExperts()