
type Exam = {
    question:string
    answer:string
    topic:string
    sub_topic:string
}
export default function Exam({exam}:{exam:Exam}){
    return(
        <>
            <section>
                
                <h3>Topic: <span>{exam.topic}</span></h3>
                <h3>SubTopic: {exam.sub_topic}</h3>
                <p>Question: {exam.question}</p>
            </section>
        </>
    )
}