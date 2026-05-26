const adjectives = [
  '清新的', '灵动的', '温暖的', '沉静的', '明亮的',
  '悠然的', '飘逸的', '淡雅的', '活泼的', '温柔的',
  '爽朗的', '恬静的', '潇洒的', '含蓄的', '热情的',
  '深沉的', '轻盈的', '从容的', '天真的', '细腻的',
  '豪放的', '婉约的', '率真的', '内敛的', '奔放的',
  '素雅的', '娇憨的', '清冽的', '醇厚的', '空灵的',
]

const nouns = [
  '微风', '山泉', '月光', '晨露', '晚霞',
  '流云', '松涛', '竹影', '梅香', '雪松',
  '碧波', '繁星', '暖阳', '秋叶', '春雨',
  '幽兰', '白鹭', '青竹', '红叶', '碧海',
  '晴空', '远山', '近水', '古树', '新芽',
  '飞鸟', '游鱼', '鸣蝉', '归燕', '落英',
]

function getRandomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)]
}

function getRandomSuffix() {
  return String(Math.floor(1000 + Math.random() * 9000))
}

export function generateGuestName() {
  const key = 'blog_guest_name'
  const stored = sessionStorage.getItem(key)
  if (stored) return stored

  const name = `${getRandomItem(adjectives)}${getRandomItem(nouns)}#${getRandomSuffix()}`
  sessionStorage.setItem(key, name)
  return name
}