import { parseAnswer } from "../functions/parse"
type Question = {
    question:string
    answer:string
    topic:string
    sub_topic:string
}
export default function Question({question}:{question:Question}){
    const answer = parseAnswer("example 123")
    console.log(`Numeric Answer: ${answer}`)
    return(
        <>
            <section>
                <h3>Topic: <span>{question.topic}</span></h3>
                <h3>SubTopic: {question.sub_topic}</h3>
                <p>Question: {question.question}</p>
                <input type="text" />
            </section>
        </>
    )
}