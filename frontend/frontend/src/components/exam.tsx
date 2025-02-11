
interface Exam {
    question:string
    answer:string
    topic:string
    sub_topic:string
}
export default function Exam({exam}:{exam:Exam}){
    return(
        <>
            <section>
                
                <h3>Topic:$'${exam.topic +" "+ exam.sub_topic}'</h3>
                <p>{exam.question}</p>
            </section>
        </>
    )
}