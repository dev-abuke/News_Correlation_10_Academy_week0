import React, { useState, useEffect } from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export default function PieSentiment(da) {
    const [topMessages, setTopMessages] = useState([]);
    const data = {
        labels: ['Positive', 'Neutral', 'Negative'],
        datasets: [
          {
            label: '# of Votes',
            data: [topMessages.Positive,topMessages.Neutral,topMessages.Negative],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)',
            ],
            borderWidth: 1,
          },
        ],
      };
    useEffect(() => {
      // Fetch data from the API endpoint
      fetch("http://127.0.0.1:5000/sentiment_stat")
        .then((response) => response.json())
        .then((data) => setTopMessages(data.sentiments))
        .catch((error) => console.error("Error fetching data:", error));
    }, []);


  return <Pie data={data} />;
}