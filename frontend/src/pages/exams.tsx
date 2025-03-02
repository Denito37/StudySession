import Question from "../components/question.tsx";
import { queryQuestions } from "../api/api.ts";
export default function Exams(){
    const url = "http://localhost:8000/Questions"
     const questions = queryQuestions(url)
    return(
        <>
        </>
    )
}