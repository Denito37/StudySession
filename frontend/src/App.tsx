import './App.css'
import './components/question.tsx'
import { queryQuestions } from './api/api.ts'
import Question from './components/question.tsx'
import Header from './components/header.tsx'
import Footer from './components/footer.tsx'
import { useEffect, useState } from 'react'

type apiResponse = {
  id:number
  question:string
  answer:string
  topic:string
  sub_topic:string
}

type ExamProps = {
  url:string;
  param?:string
}
const url:string = "http://localhost:8000/Question"
const param:string = ""

const Exam:React.FC<ExamProps> =({url, param}) =>{
  const [questions,setQuestions] = useState<apiResponse[]>([])

  useEffect(()=>{
    const getQuestions = async () => {
      const data = await queryQuestions(url,param)
      setQuestions(data)
    }
    getQuestions()
  },[url, param])

  return(
    <>
      {questions.map((question)=>(
        <Question key={question.id} question={question} />
      ))}
    </>
  )
}

function App() {
  return (
    <>   
      <Header />
      <Exam url={url} param={param} />
      <Footer />
    </>
  )
}

export default App
