package com.cums.image;

import java.time.LocalDate;
import java.time.YearMonth;
import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DiaryController {

    @GetMapping("/diary")
    public String diary(Model model) {
        YearMonth currentYearMonth = YearMonth.now();
        LocalDate today = LocalDate.now();
        List<LocalDate> dates = new ArrayList<>();
        List<String> daysOfWeek = List.of("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");

        for (int day = 1; day <= currentYearMonth.lengthOfMonth(); day++) {
            dates.add(currentYearMonth.atDay(day));
        }

        // 이번 달 첫 번째 날의 요일을 계산하여 빈 칸 추가
        int firstDayOfWeek = currentYearMonth.atDay(1).getDayOfWeek().getValue() % 7;
        for (int i = 0; i < firstDayOfWeek; i++) {
            dates.add(0, null);  // 빈 칸 추가
        }

        model.addAttribute("dates", dates);
        model.addAttribute("today", today);
        model.addAttribute("year", currentYearMonth.getYear());
        model.addAttribute("month", currentYearMonth.getMonthValue());
        model.addAttribute("daysOfWeek", daysOfWeek);


        return "diary";
    }
}
