import { useEffect, useState } from "react";
import { Card, Title, AreaChart } from "@tremor/react";

const AreaChartCard = () => {
  const [chartdata, setChartdata] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/articles");
        const data = await response.json();
        setChartdata(data.articles);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const valueFormatter = (number) => {
    return `${new Intl.NumberFormat("us").format(number).toString()} texts`;
  };

  return (
    <Card className="mt-4 bg-green-900">
      <Title>News Publishing Over Time</Title>
      <AreaChart
        className="h-72 mt-4"
        data={chartdata}
        index="date"
        categories={["all-community-building", "all-resources"]}
        colors={["indigo", "cyan"]}
        valueFormatter={valueFormatter}
      />
    </Card>
  );
};

export default AreaChartCard;
