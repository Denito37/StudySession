
export function parseAnswer(answer:string):number{
    const splitAnswer = answer.split(' ')
    let numericAnswer
    for(const word of splitAnswer){
        if(!Number.isNaN(word)){
            numericAnswer = word
        }
    }
    return Number(numericAnswer)

}