import { useEffect, useState } from "react";
import { Card, Title, AreaChart, LineChart } from "@tremor/react";
import { Line } from "react-chartjs-2";

const AreaChartCard = () => {
  const [chartdata, setChartdata] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/date_article");
        const data = await response.json();
        // Assuming 'data' contains the fetched data
        const sortedData = [...data.data]; // Create a copy of the original data array
        sortedData.sort((a, b) => new Date(a.date) - new Date(b.date));
        
        // If you need to push the sorted objects into a new array
        const sortedDataArray = [];
        sortedData.forEach(item => {
          sortedDataArray.push(item);
        });
        
        // 'sortedDataArray' now contains the sorted objects by date
        console.log(sortedDataArray);
        // console.log("sorted data : ", sortedData)
        setChartdata(sortedDataArray);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const valueFormatter = (number) => {
    return `${new Intl.NumberFormat("us").format(number).toString()} texts`;
  };

  const lineChartOptions = {
    elements: {
      point: {
        radius: 5, // Adjust the radius of the data points
        backgroundColor: 'red', // Set the background color of the data points
        borderColor: 'blue', // Set the border color of the data points
        borderWidth: 2 // Set the border width of the data points
      }
    },
    // Other chart options
  };

  return (
    <Card className="mt-4">
      <Title>News Publishing Over Time</Title>
      <AreaChart
      tickGap={1}
        className="h-72 mt-4"
        data={chartdata}
        yAxisWidth={65}
        index="date"
        categories={["articles"]}
        colors={['indigo', 'cyan']}
      />
    </Card>
  );
};

export default AreaChartCard;
