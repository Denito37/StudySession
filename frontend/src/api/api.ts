import axios from "axios";
type apiResponse = {
        id:number
        question:string
        answer:string
        topic:string
        sub_topic:string
}

async function callApi(url:string, param:string = ""):Promise<apiResponse[]> {
        const getQuestions = await axios.get(`${url}${param}`).then((response)=>{
                if(response.status !== 200){
                        console.log("Error")
                }
                if(response.data == null)
                        console.log("no data")
                return response.data as apiResponse[]
        })
        return getQuestions
}
export async function queryQuestions(url:string, param?:string):Promise<apiResponse[]> {
        const questions = await callApi(url,param)
        console.log(questions)
        return questions
}