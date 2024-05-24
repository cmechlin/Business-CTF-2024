// App.tsx
import React, { useState } from 'react'
import { tpm } from './tpm'

const App: React.FC = () => {
  const [input, setInput] = useState<string>('')
  const [backdoor, setBackdoor] = useState<string>('')
  const [output, setOutput] = useState<string>('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    const result = tpm(input, backdoor)
    setOutput(result)
  }

  return (
    <div>
      <h1>TPM Simulator</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Data Input (16-bit):
          <input
            type="text"
            value={data}
            onChange={(e) => setData(e.target.value)}
            maxLength={16}
          />
        </label>
        <label>
          Backdoor (16-bit):
          <input
            type="text"
            value={data}
            onChange={(e) => setData(e.target.value)}
            maxLength={16}
          />
        </label>
        <button type="submit">Simulate</button>
      </form>
      <div>
        <h2>Output</h2>
        <p>{output}</p>
      </div>
    </div>
  )
}

export default App
