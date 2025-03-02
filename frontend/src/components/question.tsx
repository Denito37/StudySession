
type Question = {
    question:string
    answer:string
    topic:string
    sub_topic:string
}
export default function Question({question}:{question:Question}){
    return(
        <>
            <section>
                <h3>Topic: <span>{question.topic}</span></h3>
                <h3>SubTopic: {question.sub_topic}</h3>
                <p>Question: {question.question}</p>
            </section>
        </>
    )
}