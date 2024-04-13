import {
  HiHome,
  HiChartBar,
  HiDocumentDownload,
  HiMail,
  HiCreditCard,
  HiBell,
  HiArrowUp,
  HiOutlineExternalLink,
  HiChatAlt2
} from "react-icons/hi";

import {BsAirplaneFill } from "react-icons/bs"

const Sidebar = () => {
  return (
    <div className="bg-slate-800 flex-none sm:w-20 h-screen w-32">
      <div className="h-20 items-center flex">
        <BsAirplaneFill className="text-[40px] text-gray-300 left-3 sm:left-6 fixed" />
      </div>
      <div className="fixed left-3 sm:left-6 top-[100px]">
        <HiChartBar className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
        <HiDocumentDownload className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
        <HiMail className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
        <HiCreditCard className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
        <HiBell className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
      </div>
      <div className="fixed bottom-4 left-3 sm:left-6">
        <a href="#top">
          <HiArrowUp className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
        </a>
        <HiOutlineExternalLink className="text-[40px] bg-gray-600 p-2 rounded-lg mb-4 text-gray-300" />
      </div>
    </div>
  );
};

export default Sidebar;
