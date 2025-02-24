import './App.css'
import './components/exam.tsx'
import Exam from './components/exam.tsx'
import Header from './components/header.tsx'

function App() {
  const exam_one = {question: "hi", answer:"bye", topic:"greeting", sub_topic:"greeting"}

  return (
    <>   
      <Header />
      <Exam exam={exam_one} />
    </>
  )
}

export default App
