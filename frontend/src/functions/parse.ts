
export function parseAnswer(answer:string):number{
    const splitAnswer = answer.split(' ')
    const numericAnswer = splitAnswer.filter(word =>!Number.isNaN(Number(word)))

    return Number(numericAnswer[0])
}