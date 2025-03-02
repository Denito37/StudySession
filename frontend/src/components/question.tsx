import { FormEvent, useState } from "react"
import { parseAnswer } from "../functions/parse"
type Question = {
    question:string
    answer:string
    topic:string
    sub_topic:string
}
export default function Question({question}:{question:Question}){
    const [answer,setAnswer] = useState<string>("")
    const [result,setResult] = useState<boolean>(false)
    const handleInput = (input:React.ChangeEvent<HTMLInputElement>) =>{
        setAnswer(input.target.value)
    }
    const handleSubmit = (e:FormEvent<HTMLButtonElement>)=>{
        e.preventDefault()
        if(!Number.isNaN(Number(question.answer))){
            const submittedAnswer = parseAnswer(answer)
            console.log(submittedAnswer)
            if(submittedAnswer === Number(question.answer)) setResult(true)
            else setResult(false)
        }
        else if(answer == question.answer){
            setResult(true)
        }
        else{
            setResult(false)
        }
    }

    return(
        <>
            <section>
                <h3>Topic: <span>{question.topic}</span> : {question.sub_topic}</h3>
                <p><span>Questions</span>: {question.question}</p>
                <input type="text" value={answer} onChange={handleInput} />
                <button type="submit" onClick={handleSubmit}>{result == true? "correct": "Submit"}</button>
            </section>
        </>
    )
}