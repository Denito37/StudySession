import './App.css'
import './components/question.tsx'
import { queryQuestions } from './api/api.ts'
import Question from './components/question.tsx'
import Header from './components/header.tsx'
import Footer from './components/footer.tsx'
import { FormEvent, useState } from 'react'

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
  func?:(e: React.ChangeEvent<HTMLInputElement>) => void
  limit?:(e: React.ChangeEvent<HTMLInputElement>) => void
}

const url:string = "http://localhost:8000/Question"

const Exam:React.FC<ExamProps> =({url, param, func, limit}) =>{
  const [questions,setQuestions] = useState<apiResponse[]>([])

  const getQuestions = async (param:string ="") => {
    const data = await queryQuestions(url,param)
    setQuestions(data)
  }
  const handleSubmit = async(e:FormEvent)=>{
    e.preventDefault()
    getQuestions(param)
  }

  return(
    <>
    <form action="">
      <input type="text" placeholder='Topic' onChange={func} /> 
      <input type='text' placeholder='Number of questions' onChange={limit} />
      <button type='submit' onClick={handleSubmit}>Generate Exam</button>
    </form>
      {questions.map((question)=>(
        <Question key={question.id} question={question} />
      ))}
    </>
  )
}

function App() {
  const [queryParams, setQueryParams] = useState<string>("")

  const handleValueChange = (input:React.ChangeEvent<HTMLInputElement>)=>{
    setQueryParams(`/${input.target.value}`)
  }
  const handlelimitChange =(input:React.ChangeEvent<HTMLInputElement>)=>{
    setQueryParams(`/?n=${input.target.value}`)
  }
  return (
    <>   
      <Header />
      <Exam url={url} param={queryParams} func={handleValueChange} limit ={handlelimitChange} />
      <Footer />
    </>
  )
}

export default App
