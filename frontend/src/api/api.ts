import axios from "axios";

const url = "http://localhost:8000/Questions"
export function queryQuestions(url:string, param?:string){
        axios.get(url + param).then((response)=>{
                if(response.status === 200){
                        const questions = response.data()
                        console.log(questions)
                }
        })
}