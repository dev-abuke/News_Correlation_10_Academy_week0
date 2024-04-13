import React, { useState, useEffect } from "react";
import {
  Card,
  Table,
  TableHead,
  TableRow,
  TableHeaderCell,
  TableBody,
  TableCell,
  Text,
  Title,
  Badge,
} from "@tremor/react";
import { HiOutlineStatusOnline } from "react-icons/hi";

const MAX_WORDS = 2; // Set your desired maximum word limit

const truncateText = (text) => {
  const words = text.split(" ");
  if (words.length > MAX_WORDS) {
    return words.slice(0, MAX_WORDS).join(" ") + " ...";
  }
  return text;
};

const TableCard = () => {
  const [topMessages, setTopMessages] = useState([]);

  useEffect(() => {
    // Fetch data from the API endpoint
    fetch("http://127.0.0.1:5000/top_sources")
      .then((response) => response.json())
      .then((data) => setTopMessages(data.top_channel_messages))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <Card className="mt-4">
      <Title>List of Top 10 News Outlets</Title>
      <Table className="mt-5">
        <TableHead>
          <TableRow>
            <TableHeaderCell>Source Name</TableHeaderCell>
            <TableHeaderCell>Average Sentiment</TableHeaderCell>
            <TableHeaderCell>Article Count</TableHeaderCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {topMessages.map((item, index) => (
            // Check if the text is not empty or contains only spaces
            item.source.trim() !== "" && (
              <TableRow key={index}>
                <TableCell>{item.source}</TableCell>
                <TableCell>
                  <Text>{item.score}</Text>
                </TableCell>
                <TableCell>
                  <Badge color="emerald">{item.count}</Badge>
                </TableCell>
              </TableRow>
            )
          ))}
        </TableBody>
      </Table>
    </Card>
  );
};

export default TableCard;
