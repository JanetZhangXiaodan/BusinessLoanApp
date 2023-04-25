import React, { useState } from "react";
import styled from "styled-components";

const FormContainer = styled.div`
  color: black;
  font-size: 20px;
  background-color: lightblue;
  padding: 10px 20px;
`
const Title = styled.div`
  color: black;
  font-size: 35px;
  margin: 20px;
  line-height: 50px;
  height: 50px;
  text-align: center;
`
function FormApp() {
  const [name, setName] = useState("");
  const [yearEstablished, setyearEstablished] = useState("");
  const [loanAmount, setloanAmount] = useState("");
  const [accountingProvider, setAccountingProvider] = useState('');
  const [profitOrLoss, setprofitorloss] = useState("");
  const [assetsValue, setassetsvalue] = useState("");
  const [balancesheetInfo,setbalancesheetInfo] = useState("");
  const [finalOutcome, getfinaloutcome] = useState();

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Generating loan outcome');
  };

  const handleOptionChange = (event) => {
    setAccountingProvider(event.target.value);
  };

  const RequestBalanceSheet = async () => {
    if (!name || !yearEstablished || !loanAmount) {
      return;
    }
  
    const requestInfo = {
      businessdetails: {name: name, year: yearEstablished, loanAmount: loanAmount},
      accountprovider: accountingProvider,
    };
  
    try {
      const response = await fetch("http://localhost:8080/balancesheet", {
        method: "POST",
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestInfo),
      });
      
      if (!response.ok) {
        throw new Error("Failed to fetch balance sheet data");
      }
  
      const data = await response.json();
      console.log('data', data);
      setassetsvalue(data.assetsValue);
      setprofitorloss(data.profitOrLoss);
      setbalancesheetInfo(JSON.stringify(data));
    } catch (error) {
      console.error('There was an error!', error);
    }
    console.log('Balance sheet generated!');
  };
  
  const GetFinalOutcome = async () => {
    if (!name || !yearEstablished || !profitOrLoss || !assetsValue || !loanAmount || !balancesheetInfo) {
      return;
    }

    const requestInfo = {
      businessdetails: {name: name, year: yearEstablished },
      profitOrLoss, assetsValue, loanAmount };

      console.log(requestInfo);
      
    try {
      const response = await fetch("http://localhost:8080/finaloutcome", {
        method: "POST",
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json", 
        },
        body: JSON.stringify(requestInfo),
      });
  
      if (!response.ok) {
        throw new Error("Failed to process loan request");
      }
  
      const data = await response.json();
      console.log(data);
  
      getfinaloutcome(JSON.stringify(data));
    } catch (error) {
      console.error('There was an error!', error);
    }
    console.log('Final Outcome Button clicked!');
  };
  

  return (<>
    <Title>Business Loan Application</Title>
    <FormContainer className="App">
    <form onSubmit={handleSubmit}>
    
      <label>
        Company Name:
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <br />
      <label>
        Year established:
        <input type="date" value={yearEstablished} onChange={(e) => setyearEstablished(e.target.value)} />
      </label>
      <br />
      <label>
        Loan amount (Larger than zero):
        <input type="number" value={loanAmount} onChange={(e) => setloanAmount(e.target.value)} />
      </label>
      <br />
      <label>
        Accounting provider:
        <select id="dropdown" value={accountingProvider} onChange={handleOptionChange}>
            <option value="">Choose an option</option>
            <option value="Xerox">Xerox</option>
            <option value="MYOB">MYOB</option>
        </select>
      </label>
      <br />
      <label>
        Request Balance Sheet:
        <button type="button" onClick={RequestBalanceSheet}>Request!</button>
        <label>
          Profit or Loss:
          <input name='profitOrLoss' value={profitOrLoss} readOnly/>
        </label>
        <label>
          Asset Value 
        <input name='assetsValue' value={assetsValue} readOnly/>
        </label>  
        <label>
          Yearly Balance Sheet
        <textarea rows = "20" cols="60" name='balancesheetInfo' value={balancesheetInfo} readOnly>
        </textarea>
        </label>
      </label>
      <br />
      

    <Title>Kindly review before submitting application</Title>
    <label>
        Submit Application:
        <button type="submit"onClick={GetFinalOutcome}>Submit!</button>
    </label>
    <br />
    <label>
        Final Outcome:
        <textarea rows = "5" cols="40" name='getfinaloutcome' value={finalOutcome} readOnly>
        </textarea>
    </label>
    <br />
    </form>
    </FormContainer> 
    </>);
}

export default FormApp;