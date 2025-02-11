import './App.css'
import './components/exam.tsx'
import Exam from './components/exam.tsx'

function App() {
  const exam_one = {question: "hi", answer:"bye", topic:"greeting", sub_topic:"greeting"}

  return (
    <>   
    <h1>
      STUDY SESSION EXAM
    </h1>
    <Exam exam={exam_one} />
    </>
  )
}

export default App
