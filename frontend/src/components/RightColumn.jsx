import SentimentCard from "./SentimentCard";
import ChannelAnalyticsCard from "./ChannelAnalyticsCard";
import PieSentiment from "./PieSentiment"

const RightColumn = () => {
  return (
    <div className="w-full p-2 mt-3">
      <ChannelAnalyticsCard />
      <SentimentCard />
      <PieSentiment/>
    </div>
  );
};

export default RightColumn;
