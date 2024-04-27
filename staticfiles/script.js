function changeLogo(sectionName) {
  document.getElementById("logo").textContent = sectionName;
}

window.onload = function () {
  showContent("random-facts-container");
  changeLogo("Random Facts generator");
  TabNavigation();

  var defaultNavLink = document.querySelector(".nav-link[data-category]");
  if (defaultNavLink) {

    defaultNavLink.classList.add("selected-link");
  }

  document.querySelectorAll(".nav-link").forEach(function (link) {
    link.addEventListener("click", function (event) {
    
      document.querySelectorAll(".nav-link").forEach(function (tab) {
        tab.classList.remove("selected-link");
      });
     
      this.classList.add("selected-link");

      event.preventDefault();
      var contentId = this.getAttribute("data-category");
      showContent(contentId);
    });
  });
};

function showContent(contentId) {
  document.querySelectorAll(".section").forEach(function (container) {
    container.style.display = "none";
  });

  var selectedContent = document.getElementById(contentId);
  if (selectedContent) {
    selectedContent.style.display = "block";
  }
}

function TabNavigation() {
  document.querySelectorAll(".image-section").forEach(function (section) {
    section.style.display = "none";
  });

  var defaultTab = document.querySelector(".tab-btn button[data-category]");
  if (defaultTab) {
    var defaultTabCategory = defaultTab.getAttribute("data-category");
    var defaultSection = document.getElementById(defaultTabCategory);
    if (defaultSection) {
      defaultSection.style.display = "block";
    }
    defaultTab.classList.add("selected-tab");
  }

  document.querySelectorAll(".tab-btn button").forEach(function (button) {
    button.addEventListener("click", function () {
      document.querySelectorAll(".tab-btn button").forEach(function (tab) {
        tab.classList.remove("selected-tab");
      });

      this.classList.add("selected-tab");

      var category = this.getAttribute("data-category");
      showContentTab(category);
    });
  });
}

function showContentTab(contentId) {
  document.querySelectorAll(".image-section").forEach(function (section) {
    section.style.display = "none";
  });
  var selectedSection = document.getElementById(contentId);
  if (selectedSection) {
    selectedSection.style.display = "block";
  }
}
