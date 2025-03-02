import './App.css'
import './components/question.tsx'
import Question from './components/question.tsx'
import Header from './components/header.tsx'

function App() {
  const exam_one = {question: "hi", answer:"bye", topic:"greeting", sub_topic:"greeting"}

  return (
    <>   
      <Header />
      <Question question={exam_one} />
    </>
  )
}

export default App
